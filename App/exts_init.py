from App.models import db

from flask_restful import Api

api = Api()


def ext_init(app):
    db.init_app(app)
    api.init_app(app)
