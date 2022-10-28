from DataBase.DataBase import db_model
from DataBase.DataBase import db_column
from DataBase.DataBase import db


class User(db_model):
    __tablename__ = "user"
    login_name = db_column(db.String, primary_key=True)
    password = db_column(db.String)
    authenticated = db_column(db.Boolean, default=False)
    active = False
    anonymous = False

    def __init__(self, login_name, password):
        self.login_name = login_name
        self.password = password

    def is_active(self):
        """True, as all users are active."""
        self.active = True
        return self.active

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.login_name

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_anonymous(self):
        self.anonymous = False
        return self.anonymous
