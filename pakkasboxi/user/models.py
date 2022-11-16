from pakkasboxi.database import Column, Model, SurrogatePK, db
from pakkasboxi.extensions import bcrypt
import datetime as dt

class User(SurrogatePK, Model):

    __tablename__ = "users"
    username = Column(db.String(80), unique=True, nullable=False)
    password = Column(db.Binary(128), nullable=True)
    created_at = Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)
    updated_at = Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)
    token: str = ""

    def __init__(self, username, password=None, **kwargs):
        db.Model.__init__(self, username=username, **kwargs)
        if password:
            self.set_password(password)
        else:
            self.password = None

    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password)

    def check_password(self, input_password):
        return bcrypt.check_password_hash(self.password, input_password)

    def __repr__(self):
        return str(self.username)
