from flask import request, render_template, url_for
from flask.views import MethodView
from werkzeug.utils import redirect
import trip_model

class Index(MethodView):
    def get(self):
        """
        Render the landing page for the site.
        """
        model = trip_model.get_model()
        docs = model.select()

        return render_template('index.html', docs=docs)

    def post(self):
        '''
        Pass document name and query location
        '''
        return redirect(url_for('create'))
      