from flask import render_template
from flask.views import MethodView
import review_model

class Index(MethodView):
    def get(self):
        """
        Render the landing page for the site.
        """
        return render_template('index.html')
<<<<<<< HEAD
        # model = review_model.get_model()
        # entries = [dict(name=row[0], email=row[1], signed_on=row[2], message=row[3] ) for row in model.select()]
        # return render_template('index.html',entries=entries)
=======
>>>>>>> update
