from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import trip_model
import os, datetime, string

MAP_MODE = 'place'
MAP_API_KEY = os.environ.get('MAP_KEY')

class Update(MethodView):
    def get(self):
        """
        Retrieve a single review from previously submitted ones to allow user to update information
        Uses the query parameter in the url ('entry') to retrieve the correct entry using id.
        """
        id = request.args.get('id')
        
        model = trip_model.get_model()
        doc = model.select_one(id)
        doc['map_url'] = f'https://www.google.com/maps/embed/v1/{MAP_MODE}?key={MAP_API_KEY}&q={doc["city"]}+{doc["state"]}+{doc["country"]}&maptype=satellite' 

        start = doc['start_date']
        start_date = start.split('/')
        stdate = []
        for d in start_date:
            if int(d) < 10:
                format = f'0{d[0]}'
                stdate.append(format)
            else:
                stdate.append(d)
        
        start_date_iso = f'{stdate[2]}-{stdate[0]}-{stdate[1]}'

        doc['start_date'] = start_date_iso

        end = doc['end_date']
        end_date = end.split('/')
        endate = []
        for d in end_date:
            if int(d) < 10:
                format = f'0{d[0]}'
                endate.append(format)
            else:
                endate.append(d)
        end_date_iso = f'{endate[2]}-{endate[0]}-{endate[1]}'
        doc['end_date'] = end_date_iso

        loc_data = dict(city=doc['city'], state=doc['state'], country=doc['country'])
        links = model.get_article_data(loc_data)
        forecast = model.get_weather_data(loc_data)

        return render_template('update.html', links=links, doc=doc, forecast=forecast)

    def post(self):
        """
        Take form data from updated review entry and send update query to edit entry in the database.
        Redirects to the landing page.
        """
        model = trip_model.get_model()

        id = request.args.get('id') 
        start = datetime.datetime.fromisoformat(request.form['start_date'])
        end = datetime.datetime.fromisoformat(request.form['end_date'])
        start_date = f'{start.month}/{start.day}/{start.year}'
        end_date = f'{end.month}/{end.day}/{end.year}' 
        
        location = request.form['location']
        location = location.split(',')

        trip_details = dict(title=request.form['title'],
                            notes=request.form['notes'], 
                            start_date=start_date, 
                            end_date=end_date, 
                            city=location[0], state=location[1], 
                            country=location[2],
                            id=id)
        
        model.update(trip_details)
        return redirect(url_for('index'))
