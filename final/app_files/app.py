"""
This code has been adapted from https://github.com/wu4f/cs430-src
"""
import flask
from index import Index
from update import Update
from create import Create

app = flask.Flask(__name__)       # our Flask app

app.add_url_rule('/',
                 view_func=Index.as_view('index'),
                 methods=['GET', 'POST'])

app.add_url_rule('/update',
                  view_func=Update.as_view('update'),
                  methods=['GET', 'POST'])

app.add_url_rule('/create',
                  view_func=Create.as_view('create'),
                  methods=['GET', 'POST'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)