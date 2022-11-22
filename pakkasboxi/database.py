from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from .extensions import db
from .settings import DevConfig

Column = db.Column
relationship = relationship
Model = db.Model
engine = create_engine(DevConfig.SQLALCHEMY_DATABASE_URI)

class SurrogatePK(object):

    __table_args__ = {"extend_existing": True}
    id = db.Column(db.Integer, primary_key=True)

    @classmethod
    def get_by_id(cls, record_id):
        with Session(engine) as session:
            return session.get(cls, int(record_id))

    @classmethod
    def get_all(cls):
        with Session(engine) as session:
            return session.query(cls).all()

    @classmethod
    def get_all_ids(cls):
        with Session(engine) as session:
            return [id[0] for id in session.query(cls.id).all()]

