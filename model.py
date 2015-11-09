"""Models and database functions for EEG tracking project."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

##############################################################################
# Model definitions

class User(db.Model):
    """User of lama log website."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.string(64), nullable=True)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<User user_id=%s email=%s>" (self.user_id, self.email)



class Session(db.Model):
    """Running time of a session."""
    
    __tablename__ = "sessions"
    
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    utc = db.Column(db.String(64), nullable=True)

    def __repr__(self):
        return "<UTC:%s>" % (self.utc)


class State(db.Model):
    """Cognition values."""
    
    __tablename__ = "states"
    
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    utc = db.Column(db.String(64), nullable=True)
    attention = db.Column(db.Integer, nullable=True)
    meditation = db.Column(db.Integer, nullable=True)
    session_id = db.Column(db.Integer, db.ForeignKey('sessions.utc'))


    def __repr__(self):
        return "<UTC:%s, Attention:%d, Meditation:%d>" % (self.utc, self.attention, self.meditation)

    


##############################################################################
# Helper functions

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our SQLite database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lamalog.db'
    app.config['SQLALCHEMY_ECHO'] = True
    db.app = app    
    db.init_app(app)


if __name__ == "__main__":
    from server import app
    connect_to_db(app)
    print "Connected to DB."
