from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import review_model

class Update(MethodView):
    def get(self):
        """
        Retrieve a single review from previously submitted ones to allow user to update information
        Uses the query parameter in the url ('entry') to retrieve the correct entry using id.
        """
        id = request.args.get('id')
        
        model = review_model.get_model()
        review = model.select_one(id)

        entry = {'name':review[0], 'number':review[1], 'dept':review[2], 'quarter':review[3], 'year':review[4], 
            'instructor':review[5], 'rating':review[6], 'review':review[7], 'id':id}
             
        return render_template('update.html', entry=entry)

    def post(self):
        """
        Take form data from updated review entry and send update query to edit entry in the database.
        Redirects to the landing page.
        """
        rating_number = int(request.form['rating'])
        # get id from url args
        id = request.args.get('id')

        model = review_model.get_model() 
        model.update(id, request.form['name'], request.form['number'], request.form['dept'], request.form['quarter'], request.form['year'], request.form['instructor'], rating_number, request.form['review'])
        return redirect(url_for('index'))
