import flask
import calendar
from flask import request
from datetime import date
from datetime import datetime
app = flask.Flask(__name__)
app.config["DEBUG"] = True
@app.route('/', methods=['GET'])
def home():
    return "<h1>Weekday Finder App</h1>\n<p>Use /wday url extension to find the day of the week using date stamp.\nPass the required date as 'dt' argument. Use 'dd/mm/yyyy' format.</p>"
@app.route('/wday', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'dt' in request.args:
        dt = request.args['dt']
    else:
        return "Error: No Date field provided.Please specify a Date as 'dt' argument. Use 'dd/mm/yyyy' format."
    cdobj = datetime.strptime(dt,'%d/%m/%Y')
    wday = calendar.day_name[cdobj.weekday()]
    return ("The weekday of ({}) is: {}".format(dt,wday))
app.run()
