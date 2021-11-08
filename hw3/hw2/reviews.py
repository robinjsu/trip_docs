from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import review_model

class Reviews(MethodView):
    def get(self):
        """
        Render the page with list of previously entered course reviews.
        This page renders database entries, as well as options to update existing entries.
        """
        model = review_model.get_model()
        
        entries = [dict(name=row[0], number=row[1], dept=row[2], quarter=row[3], year=row[4], 
            instructor=row[5], rating=row[6], review=row[7] ) for row in model.select()]
        
        for e in entries:
            e['rating'] = int(e['rating'])
             
        return render_template('reviews.html', entries=entries)