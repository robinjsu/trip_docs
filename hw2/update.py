from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import review_model

class Update(MethodView):
    def get(self, id):
        model = review_model.get_model()
        