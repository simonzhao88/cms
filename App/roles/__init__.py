from flask import Blueprint


role = Blueprint('roles', __name__)


from . import role_views