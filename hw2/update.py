from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import review_model

class Update(MethodView):
    def get(self):
        """
        Retrieve a single review from previously submitted ones to allow user to update information
        Uses the query parameter in the url ('entry') to retrieve the correct entry using id.
        """
        model = review_model.get_model()

        id = request.args.get('entry')
        review = model.select_one(id)
        
        entry = {'name':review[0], 'number':review[1], 'dept':review[2], 'quarter':review[3], 'year':review[4], 
            'instructor':review[5], 'rating':review[6], 'review':review[7]}
             
        return render_template('update.html', entry=entry, id=id)

    def post(self):
        """
        Take form data from updated review entry and send command to update the entry in the database
        """
        rating_number = int(request.form['rating'])
        assert (rating_number >= 0 and rating_number <=5), f"Ratings error: {request.form['rating']}"
        # assert request.content_length < int.__sizeof__
        id = request.referrer[-1]
        print(f"id: {id}")

        model = review_model.get_model() 
        model.update(id, request.form['name'], request.form['number'], request.form['dept'], request.form['quarter'], request.form['year'], request.form['instructor'], rating_number, request.form['review'])
        return redirect(url_for('index'))
