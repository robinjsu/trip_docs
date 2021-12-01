import os
from datetime import date
from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import trip_model

MAP_MODE = 'place'
MAP_API_KEY = os.environ.get('MAP_KEY')

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
        model = trip_model.get_model()
        if (save == True):
            pass

        else:
            start = date.fromisoformat(request.form['start_date'])
            end = date.fromisoformat(request.form['end_date'])
            start_date = f'{start.month}/{start.day}/{start.year}'
            end_date = f'{end.month}/{end.day}/{end.year}' 
            city = request.form['city']
            state = request.form['state']
            country = request.form['country']
            
            map_url=f'https://www.google.com/maps/embed/v1/{MAP_MODE}?key={MAP_API_KEY}&q={city}+{state}+{country}&maptype=satellite'
            info = dict(trip=request.form['trip'], start_date=start_date, end_date=end_date, city=request.form['city'], country=request.form['country'], map_url=map_url)
            
            links = model.get_article_data(dict(city=city, state=state, country=country))
        
        return render_template('create.html', blank=False, info=info, links=links)
        
        

