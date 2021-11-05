from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import review_model

class Submit(MethodView):
    def get(self):
        """
        Render the page where users can submit new course reviews.
        """
        return render_template('submit.html')

    def post(self):
        """
        Accepts POST requests, and processes the form;
        Redirect to index when completed.
        """
        rating_number = int(request.form['rating'])
        
        model = review_model.get_model()
        model.insert(request.form['name'], request.form['number'], request.form['dept'], 
            request.form['quarter'], request.form['year'], request.form['instructor'], rating_number,
            request.form['review'])
        return redirect(url_for('index'))
