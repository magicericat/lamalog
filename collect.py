from NeuroPy import NeuroPy
from model import connect_to_db, db, Session, State
import time
import datetime

def collect(port, user_id):
    """Collect attention and meditation values from NeuroSky headset & store to database"""

    print "You have reached the beginning of this function!"
    port = str(port)
    headset_data = NeuroPy("/dev/cu.MindWaveMobile-DevA-" + port, 57600)

    headset_data.start()
    current_time = time.time()
    start_time = time.time()
    elapsed_time = current_time + 60 # Collect data from headset for an elapsed time of a minute.
    
    new_session = Session(utc=datetime.datetime.utcnow(), user_id=user_id)
    
    # TODO: figure out how to get current_user
    # current_user.sessions.append(new_session)
    # db.session.add(current_user)
    db.session.add(new_session)
    db.session.commit()
    print new_session.id

    # Add session to database first.
    # In the while loop, save attention and meditation data to database.
    while current_time < elapsed_time:
        attention = headset_data.attention
        # print attention
        current_time = time.time()
        # print current_time, elapsed_time
        meditation = headset_data.meditation
        
        new_state = State(utc=datetime.datetime.utcnow(), attention=attention, meditation=meditation, session_id=new_session.id)
        db.session.add(new_state)
        db.session.commit()
        time.sleep(5) # Collect data every 5 seconds.

    # headset_data.stop()
    # print attention
    return

    # append the values to an array and return an array


if __name__ == "__main__":
    from server import app
    connect_to_db(app)
    print "Connected to DB."
    db.create_all()
    collect()