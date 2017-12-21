from flask_security import Security, SQLAlchemyUserDatastore

from admin import admin
from app import app, db
from models import Role, User

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)
