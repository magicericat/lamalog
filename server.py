"""Lama Log."""

from flask import Flask, render_template, request, flash, redirect, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension

import time 
import datetime

from NeuroPy import NeuroPy
from model import connect_to_db, db, Session, State, User
from collect import collect

app = Flask(__name__)

# This is required to use Flask sessions and debug toolbar.
app.secret_key = "kugel"

         
##############################################################################

@app.route('/')
def main():
    """Homepage"""

    return render_template("homepage.html")

@app.route('/about')
def about():
    """About Page"""

    return render_template("about.html")

@app.route('/collect')
def record_new_session():
    """Displays page to record new session."""

    

    return render_template("collect.html", user_id=session["user_id"])


@app.route('/collectdata', methods=['POST'])
def record():
    """Record meditation session and store in database."""

    print "Rainbows!"
    port = request.form.get("port")
    print port
    collect(port, session["user_id"])
    # Collect.py should literally be nothing more than a bridge between hardware and the data that comes out of it.
    # College.py should return an array of states. It shouldn't even know what the session is or what the user is.
    # all it should know is given a port, return the information about the user and return it back.

    
    return "Successfully collected data!"


@app.route('/register', methods=['GET'])
def register_form():
    """Show form for user signup."""

    return render_template("register_form.html")


@app.route('/register', methods=['POST'])
def register_process():
    """Process registration."""

    # Get form variables
    email = request.form["email"]
    password = request.form["password"]

    new_user = User(email=email, password=password)

    db.session.add(new_user)
    db.session.commit()

    flash("User %s added." % email)
    return redirect("/")

@app.route('/login', methods=['GET'])
def login_form():
    """Show login form."""

    return render_template("login_form.html")

@app.route('/login', methods=['POST'])
def login_process():
    """Process login."""

    # Get form variables
    email = request.form["email"]
    password = request.form["password"]

    user = User.get_user_by_email(email)
    # user = User.query.filter_by(email=email).first()

    if not user:
        flash("No such user")
        return redirect("/login")

    if user.password != password:
        flash("Incorrect password")
        return redirect("/login")

    session["user_id"] = user.user_id

    flash("Logged in")

    return redirect("/users/%s" % user.user_id)

@app.route('/logout')
def logout():
    """Log out."""

    del session["user_id"]
    flash("Logged Out.")
    return redirect("/")

@app.route('/eeg-states.json')
def eeg_states_data():
    """Return time series data of EEG States."""
    # Look up current_user with Flask
    # current_user.session....
    # from session, query all the states
    last_session = Session.query.filter_by(user_id=session["user_id"]).all()[-1]
    print "user_id", session["user_id"]

    print last_session

    all_states = State.query.filter_by(session_id=last_session.id).all()
    # TODO: Can improve this query to get all the sessions for one user and 
    # make a graph for each session. It just takes session_id=1 of whoever uses this thing.

    # Query the current user for the sessions. Session has the user_id. 

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


@app.route("/users/<int:user_id>")
def user_detail(user_id):
    """Show info about user."""

    user = User.query.get(user_id)
    return render_template("user.html", user=user)



##############################################################################
if __name__ == "__main__":

    app.debug = True
    connect_to_db(app)
    DebugToolbarExtension(app)
    app.run()

