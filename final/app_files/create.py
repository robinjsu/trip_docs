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

    def post(self):
        '''
        Saves content from page to datastore, 
        user remains on the same page after submitting the content
        '''
        model = trip_model.get_model()

        if (bool(request.args.get('save')) == True):

            location_str = request.form['location']
            location = location_str.split(',')
            
            trip_details = dict(title=request.form['title'],
                                notes=request.form['notes'], 
                                start_date=request.form['start_date'], 
                                end_date=request.form['end_date'], 
                                city=location[0], state=location[1], 
                                country=location[2])
            model.insert(trip_details)
            return redirect(url_for('index'))

        else:
            start = date.fromisoformat(request.form['start_date'])
            end = date.fromisoformat(request.form['end_date'])
            start_date = f'{start.month}/{start.day}/{start.year}'
            end_date = f'{end.month}/{end.day}/{end.year}' 
            city = request.form['city']
            state = request.form['state']
            country = request.form['country']
            
            map_url=f'https://www.google.com/maps/embed/v1/{MAP_MODE}?key={MAP_API_KEY}&q={city}+{state}+{country}&maptype=satellite'
            info = dict(trip=request.form['trip'], 
                        start_date=start_date, 
                        end_date=end_date, 
                        city=city, 
                        state=state, 
                        country=country, 
                        map_url=map_url)
            
            links = model.get_article_data(dict(city=city, state=state, country=country))
        
        return render_template('create.html', blank=False, info=info, links=links)
        
        

