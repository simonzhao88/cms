from flask import request
from flask_restful import Resource

from App.exts_init import api


class RoleApi(Resource):
    def post(self):
        role_name = request.form.get('r_name')
        return {
            'code': 200,

        }


api.add_resource(RoleApi, '/api/role/')
