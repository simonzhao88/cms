from flask import render_template, request
from flask_restful import Resource, reqparse

from App.exts_init import api
from App.models import Grade, db
from utils import status_code
from utils.login_required import login_required
from . import main


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/head/')
def head():
    return render_template('head.html')


@main.route('/left/')
def left():
    return render_template('left.html')


@main.route('/main/')
def main_page():
    return render_template('main.html')


@main.route('/grade/')
def grade():
    return render_template('grade.html')


@main.route('/addgrade/')
def add_grade():
    return render_template('addgrade.html')


@main.route('/student/')
def student():
    return render_template('student.html')


@main.route('/addstu/')
def add_stu():
    return render_template('addstu.html')


@main.route('/roles/')
def roles():
    return render_template('roles.html')


@main.route('/addRoles/')
def add_roles():
    return render_template('addroles.html')


@main.route('/permissions/')
def permissions():
    return render_template('permissions.html')


@main.route('/addPermission/')
def add_permission():
    return render_template('addpermission.html')


@main.route('/users/')
def users():
    return render_template('users.html')


@main.route('/adduser/')
@login_required
def add_user():
    return render_template('add_edit.html')


@main.route('/changepwd/')
def change_pwd():
    return render_template('changepwd.html')


class GradeApi(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('grade_name', type=str, required=True,
                                   help='请输入正确的班级名~')

    def get(self):
        grades = Grade.query.all()
        return {
            'code': 200,
            'msg': '查询成功~',
            'grades': [grade.to_dict() for grade in grades]
        }

    def post(self):
        args = self.reqparse.parse_args()
        g_name = args.get('grade_name')
        if Grade.query.filter_by(g_name=g_name):
            return status_code.GRADE_ADD_EXITS_ERROR
        gr = Grade(g_name=g_name)
        db.session.add(gr)
        db.session.commit()
        return {
            'code': 200,
            'msg': '添加班级成功~',
            'data': gr.to_dict()
        }

    def delete(self):
        pass

    def patch(self):
        pass


class StudentApi(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('s_name', type=str, required=True,
                                   help='请输入正确的学生名~')
        self.reqparse.add_argument('gender', type=bool, required=True,
                                   help='请输入正确的性别~')
        self.reqparse.add_argument('grade_id', type=int, required=True,
                                   help='请输入正确的班级名~')

    def get(self):
        pass

    def post(self):
        args = self.reqparse.parse_args()
        pass

    def delete(self):
        pass

    def patch(self):
        pass


api.add_resource(GradeApi, '/api/grade/', '/api/grade/<int:id>')
api.add_resource(StudentApi, '/api/student/')
