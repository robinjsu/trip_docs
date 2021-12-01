import os, json, requests as r
from datetime import date
from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import trip_model

MAP_MODE = 'place'
MAP_API_KEY = os.environ.get('MAP_KEY')
NYT_KEY = os.environ.get('NYT_KEY')

class Create(MethodView):
    def get(self):
        '''
        Render empty document with empty notes field, 
        retrieve map and weather for destination entered 
        :param trip_name: name entered by user on home page
        :param location: location entered by user on home page
        '''
        
        return render_template('create.html', blank=True)

    def post(self, save=False):
        '''
        Saves content from page to datastore, 
        user remains on the same page after submitting the content
        '''
        if (save == True):
            model = trip_model.get_model()

        else:
            start = date.fromisoformat(request.form['start_date'])
            end = date.fromisoformat(request.form['end_date'])
            start_date = f'{start.month}/{start.day}/{start.year}'
            end_date = f'{end.month}/{end.day}/{end.year}'

            city = request.form['city']
            state = request.form['state']
            country = request.form['country']
            map_url=f'https://www.google.com/maps/embed/v1/{MAP_MODE}?key={MAP_API_KEY}&q={city}+{state}+{country}&maptype=satellite'
            
            nyt_url = f'https://api.nytimes.com/svc/search/v2/articlesearch.json?api-key={NYT_KEY}&q={city},{state},{country}&fq=section_name:("Travel") AND glocations.contains:("{city}" "{country}")'
            response = r.get(nyt_url)
            response = response.json()
            assert response['status'] == 'OK', f'Received a non "OK" response: {response["status"]}'
            articles_list = [x for x in response['response']['docs']]
            assert len(articles_list) > 0, f'response: {response}'
            links = []
            for a in articles_list:
                item = dict(headline=a['headline']['main'], url=a['web_url'], abstract=a['abstract'])
                pub = date.fromisoformat(a['pub_date'][:10])
                item['pub_date'] = f'{pub.month}/{pub.day}/{pub.year}'
                links.append(item)

            info = dict(trip=request.form['trip'], start_date=start_date, end_date=end_date, city=request.form['city'], country=request.form['country'], map_url=map_url)
        return render_template('create.html', blank=False, info=info, links=links)
        
        

