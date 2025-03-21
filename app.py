from flask import Flask
from application.database import db
from application.models import User,Role
from application.config import LocalDevelopmentCongif
from flask_security import Security, SQLALchemyUserDatastore

def create_app():
    app = Flask(__name__)
    app.config.from_object(LocalDevelopmentCongif)
    db.init_app(app)
    datastore = SQLALchemyUserDatastore(db,User,Role)
    app.security = Security(app,datastore)
    app.app_context().push()
    return app

app = create_app()

if __name__ == "main":
    app.run()
