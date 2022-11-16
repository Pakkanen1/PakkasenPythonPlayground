from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy, Model
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt

class CRUDMixin(Model):
    """ Mixin class containing methods for (C)reating, (R)eading, (U)pdating and (D)eleting in the database """

    @classmethod
    def create(cls, **kwargs):
        instance = cls(**kwargs)
        return instance.save()

    def update(self, commit=True, **kwargs):
        for attr, value in kwargs.items():
            setattr(self, attr, value)
        return commit and self.save() or self

    def save(self, commit=True):
        db.session.add(self)
        if commit:
            db.session.commit()
        return self

    def delete(self, commit=True):
        db.session.delete(self)
        return commit and db.session.commit()


db = SQLAlchemy(model_class=CRUDMixin)
migrate = Migrate()
bcrypt = Bcrypt()