"""Lama Log."""

from flask import Flask, render_template, flash, redirect, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension

import time 
import datetime

from NeuroPy import NeuroPy
from model import connect_to_db, db, Session, State

app = Flask(__name__)

# This is required to use Flask sessions and debug toolbar.
app.secret_key = "kugel"

         
##############################################################################

@app.route('/')
def main():
    """Homepage"""

    return render_template("index.html")


@app.route('/eeg-states.json')
def eeg_states_data():
    """Return time series data of EEG States."""

    all_states = State.query.filter_by(session_id=1).all()
    # TODO: Can improve this query to get all the sessions for one user and 
    # make a graph for each session.

    # List comprehensions to feed into data_dictionary.
    meditation = [state.meditation for state in all_states]
    attention = [state.attention for state in all_states]
    labels = [datetime.datetime.strftime(state.utc, "%-M:%-S") for state in all_states]
    # Using strftime to account for jsonifying.

    data_dict = {
        "labels": labels,
        "datasets": [
            {
                "label": "Meditation",
                "fillColor": "rgba(220,220,220,0.2)",
                "strokeColor": "rgba(220,220,220,1)",
                "pointColor": "rgba(220,220,220,1)",
                "pointStrokeColor": "#fff",
                "pointHighlightFill": "#fff",
                "pointHighlightStroke": "rgba(220,220,220,1)",
                "data": meditation
            },
            {
                "label": "Attention",
                "fillColor": "rgba(151,187,205,0.2)",
                "strokeColor": "rgba(151,187,205,1)",
                "pointColor": "rgba(151,187,205,1)",
                "pointStrokeColor": "#fff",
                "pointHighlightFill": "#fff",
                "pointHighlightStroke": "rgba(151,187,205,1)",
                "data": attention
            }
        ]
    }
    return jsonify(data_dict)


@app.route('/chart')
def chart():
    """Lama Log Dashboard"""

    return render_template("mycharts.html")



##############################################################################
if __name__ == "__main__":

    app.debug = True
    connect_to_db(app)
    DebugToolbarExtension(app)
    app.run()

