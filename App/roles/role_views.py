from flask import request
from flask_restful import Resource

from App.exts_init import api
from App.models import Role, db, Permission, User
from utils import status_code


class RoleApi(Resource):
    def get(self):
        r_id = request.args.get('r_id')
        if r_id:
            role = Role.query.get(r_id)
            return {
                'code': 200,
                'role': role.to_dict()
            }
        roles = Role.query.all()
        return {
            'code': 200,
            'roles': [role.to_dict() for role in roles]
        }

    def post(self):
        role_name = request.form.get('r_name')
        p_ids = request.form.get('p_id').split(',')
        role = Role(r_name=role_name)
        permission = Permission.query.filter(Permission.p_id.in_(p_ids)).all()
        role.permission = permission
        db.session.add(role)
        db.session.commit()
        return status_code.SUCCESS

    def patch(self):
        r_id = request.form.get('r_id')
        role_name = request.form.get('r_name')
        p_ids = request.form.get('p_id').split(',')
        role = Role.query.get(r_id)
        role.r_name = role_name

        permission = Permission.query.filter(Permission.p_id.in_(p_ids)).all()
        role.permission = permission
        db.session.add(role)
        db.session.commit()
        return status_code.SUCCESS

    def delete(self):
        r_id = request.form.get('r_id')
        role = Role.query.get(r_id)
        db.session.delete(role)
        db.session.commit()
        return status_code.SUCCESS


class PermissionApi(Resource):
    def get(self):
        permissions = Permission.query.all()
        return {
            'code': 200,
            'permissions': [permission.to_dict() for permission in permissions]
        }

    def post(self):
        p_name = request.form.get('p_name')
        per = Permission(p_name=p_name)
        db.session.add(per)
        db.session.commit()
        return status_code.SUCCESS

    def delete(self):
        p_id = request.form.get('p_id')
        per = Permission.query.get(p_id)
        db.session.delete(per)
        db.session.commit()
        return status_code.SUCCESS


class UserApi(Resource):
    def get(self):
        u_id = request.args.get('u_id')
        if u_id:
            user = User.query.get(u_id)
            return {
                'code': 200,
                'user': user.to_dict()
            }
        users = User.query.all()
        return {
            'code': 200,
            'users': [user.to_dict() for user in users]
        }

    def post(self):
        username = request.form.get('username')
        pwd1 = request.form.get('pwd1')
        pwd2 = request.form.get('pwd2')
        role = request.form.get('role')
        u = User.query.filter_by(username=username).first()
        if u:
            return status_code.USER_REGISTER_EXITS_USER
        elif pwd1 != pwd2:
            return status_code.USER_REGISTER_PASSWORD_IS_NOT_VALID
        user = User(username=username, password_hash=pwd1)
        user.role_id = role
        db.session.add(user)
        db.session.commit()
        return status_code.SUCCESS

    def patch(self):
        username = request.form.get('username')
        role = request.form.get('role')
        u = User.query.filter_by(username=username).first()
        u.username = username
        u.role_id = role
        db.session.add(u)
        db.session.commit()
        return status_code.SUCCESS


api.add_resource(RoleApi, '/api/role/')
api.add_resource(PermissionApi, '/api/permission/')
api.add_resource(UserApi, '/api/user/')
