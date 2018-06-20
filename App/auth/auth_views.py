from flask import request, render_template, session, jsonify
from flask_restful import Resource, reqparse

from App.exts_init import api
from App.models import User, db
from utils import status_code
from . import auth


@auth.route('/create_db/')
def create_db():
    """
    初始建表
    :return:
    """
    db.create_all()
    db.session.commit()
    return '创建成功'


@auth.route('/login/', methods=['GET'])
def login():
    """
    渲染的登陆页面
    :return:
    """
    if request.method == 'GET':
        return render_template('login.html')


@auth.route('/register/', methods=['GET'])
def register():
    """
    渲染注册页面
    :return:
    """
    if request.method == 'GET':
        return render_template('register.html')


class LoginApi(Resource):
    """登陆API接口"""
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('username', type=str, required=True,
                                   help='用户名不合法~')
        self.reqparse.add_argument('password', type=str, required=True,
                                   help='密码不合法~')
        super(LoginApi, self).__init__()

    def post(self):
        args = self.reqparse.parse_args()
        username = args.get('username')
        password = args.get('password')
        u = User.query.filter_by(username=username).first()
        if u and u.verify_password(password):
            session['u_id'] = u.u_id
            return {
                'code': 200,
                'msg': '登陆成功~'
            }
        return status_code.USER_LOGIN_PASSWORD_ERROE


class RegisterApi(Resource):
    """注册API接口"""
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('username', type=str, required=True,
                                   help='用户名不合法~')
        self.reqparse.add_argument('password', type=str, required=True,
                                   help='密码不合法~')
        super(RegisterApi, self).__init__()

    def post(self):
        args = self.reqparse.parse_args()
        username = args.get('username')
        password = args.get('password')
        if User.query.filter_by(username=username).first():
            return status_code.USER_REGISTER_EXITS_USER
        u = User(username=username, password=password)
        db.session.add(u)
        db.session.commit()
        return {
            'code': 200,
            'msg': '注册成功'
        }


api.add_resource(LoginApi, '/auth/login/')
api.add_resource(RegisterApi, '/auth/register/')
