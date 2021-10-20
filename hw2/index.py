from flask import render_template
from flask.views import MethodView
import review_model

class Index(MethodView):
    def get(self):
        return render_template('index.html')
        # model = review_model.get_model()
        # entries = [dict(name=row[0], email=row[1], signed_on=row[2], message=row[3] ) for row in model.select()]
        # return render_template('index.html',entries=entries)
