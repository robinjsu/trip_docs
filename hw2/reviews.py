from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import gbmodel

class Reviews(MethodView):
    def get(self):
        model = gbmodel.get_model()
        
        entries = [dict(name=row[0], number=row[1], dept=row[2], quarter=row[3], year=row[4], 
            instructor=row[5], rating=row[6], review=row[7] ) for row in model.select()]
        
        for e in entries:
            e['rating'] = int(e['rating'])
             
        return render_template('reviews.html',entries=entries)