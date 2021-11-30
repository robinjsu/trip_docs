import os
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
        if (save == True):
            return redirect(url_for('index'))
        else:
            info = dict(trip=request.form['trip'], date=request.form['date'], city=request.form['city'], country=request.form['country'], map_url=f'https://www.google.com/maps/embed/v1/{MAP_MODE}?key={MAP_API_KEY}&q={city+country}&maptype=satellite')
        return render_template('create.html', blank=False, info=info)
        
        

