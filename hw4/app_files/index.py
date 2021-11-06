from flask import render_template
from flask.views import MethodView
import review_model

class Index(MethodView):
    def get(self):
        """
        Render the landing page for the site.
        """
        return render_template('index.html')
