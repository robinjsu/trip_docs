"""
This code has been adapted from https://github.com/wu4f/cs430-src
"""
import flask
from flask.globals import request
from flask.views import MethodView
from index import Index
from reviews import Reviews
from submit import Submit
from update import Update

app = flask.Flask(__name__)       # our Flask app

app.add_url_rule('/',
                 view_func=Index.as_view('index'),
                 methods=['GET'])

app.add_url_rule('/submit',
                 view_func=Submit.as_view('submit'),
                 methods=['GET', 'POST'])

app.add_url_rule('/reviews',
                 view_func=Reviews.as_view('reviews'),
                 methods=['GET'])              

app.add_url_rule('/update', 
                  view_func=Update.as_view('update'),
                  methods=['GET', 'POST'],
                  
                  )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
