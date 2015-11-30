![LamaState Logo](https://github.com/magicericat/lamastate/blob/master/static/screenshot.png)

Lama State is a meditation tool and Flask web app that interfaces with the NeuroSky headset to collect, analyze, and keep track of brainwave recordings. “Attention” and “Meditation” values range from 0 to 100 and increase when users are focused and relaxed and decrease when they are uneasy or stressed - these values are presented to users in a series of meaningful time-series graphs. Users with a NeuroSky headset will be able to record meditation sessions, compare a session against their past efforts, and even see how well they rank on a collective leaderboard. 

## Table of Contents
* [Inspiration](#inspiration)
* [Terminology](#terms)
* [Getting Started](#gettingstarted)
* [Technical Stack](#technicalstack)
* [Features](#features)
* [Author](#author)

## <a name="inspiration"></a>Inspiration
[Strava](http://www.strava.com) meets [donothingfor2minutes.com](http://www.donothingfor2minutes.com)

## <a name="terms"></a>Terminology
##### NeuroSky Mindwave Mobile Headset
![NeuroSky Mindwave Mobile Headset](https://github.com/magicericat/lamastate/blob/master/static/mindwave.jpg)

The Neurosky MindWave Mobile is an EEG headset, or brain activity monitor. The headset safely detects brainwave signals and is able to interact with the Lama State app.
##### Attention
Attention values range from 0 to 100 and indicate the intensity of mental “focus” or “attention.” The attention level increases when a user focuses on a single thought or an external object, and decreases when distracted.
##### Meditation
Meditation values ranges from 0 to 100 and indicate the level of mental “calmness” or “relaxation.” The meditation level increases when users relax the mind and decreases when they are uneasy or stressed.

## <a name="gettingstarted"></a>Getting Started

0.* Dependencies: NeuroSky EEG headset  

1. Install requirements at the command prompt if you haven't yet:

        $ pip install requirements.txt

2. Start the server:
        
        $ python server.py

3. Visit http://localhost:5000 in your web browser.

## <a name="technicalstack"></a>Technical Stack
* [Python](https://www.python.org/)
* [Flask](http://flask.pocoo.org/)
* SQLite3
* SQLAlchemy
* Javascript
* [jQuery](https://jquery.com/)
* AJAX/JSON
* [Jinja2](http://jinja.pocoo.org/docs/dev/)
* Chart.js
* HTML5/CSS3
* [Bootstrap](http://getbootstrap.com/2.3.2/)


## <a name="features"></a>Features
- User Accounts
  - Register, Login, Logout
- Record a new session
  - Wrote a collect.py script to pull data off of a bluetooth EEG headset
  - Tables for Users, Sessions, and States
  - Stores data in SQLite3 database
- Brain States Dashboard
  - After a session, a user will be able to see a graph of their meditation and attention values
  - List comprehension and Chart.js
- Leaderboard
  - Wrote a function to calculate a max meditation score 
  - SQLAlchemy queries to see rank on collective leaderboard
- Bootstrap/HTML/CSS
  - Integrated front-end styling with bootstrap
- Tests
  - Working on implementing unit tests


## <a name="author"></a>Author
Erica Johnson is a neuroscientist-turned-engineer living in San Francisco, CA.
[LinkedIn](https://www.linkedin.com/in/ericatjohnson)
