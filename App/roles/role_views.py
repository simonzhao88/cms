from flask import request
from flask_restful import Resource

from App.exts_init import api
from App.models import Role, db
from utils import status_code


class RoleApi(Resource):
    def get(self):
        roles = Role.query.all()
        return {
            'code': 200,
            'roles': [role.to_dict() for role in roles]
        }

    def post(self):
        role_name = request.form.get('r_name')
        role = Role(r_name=role_name)
        db.session.add(role)
        db.session.commit()
        return status_code.SUCCESS


api.add_resource(RoleApi, '/api/role/')
