from flask import render_template, request
from flask_restful import Resource, reqparse

from App.exts_init import api
from App.models import Grade, db, Student
from utils import status_code
from utils.login_required import login_required
from . import main


@main.route('/')
@login_required
def index():
    return render_template('index.html')


@main.route('/head/')
def head():
    return render_template('head.html')


@main.route('/left/')
@login_required
def left():
    return render_template('left.html')


@main.route('/main/')
def main_page():
    return render_template('main.html')


@main.route('/grade/')
def grade():
    return render_template('grade.html')


@main.route('/addgrade/')
@login_required
def add_grade():
    return render_template('addgrade.html')


@main.route('/student/')
def student():
    return render_template('student.html')


@main.route('/addstu/')
@login_required
def add_stu():
    return render_template('addstu.html')


@main.route('/roles/')
@login_required
def roles():
    return render_template('roles.html')


@main.route('/addRoles/')
@login_required
def add_roles():
    return render_template('addroles.html')


@main.route('/permissions/')
@login_required
def permissions():
    return render_template('permissions.html')


@main.route('/addPermission/')
@login_required
def add_permission():
    return render_template('addpermission.html')


@main.route('/users/')
@login_required
def users():
    return render_template('users.html')


@main.route('/adduser/')
@login_required
def add_user():
    return render_template('add_edit.html')


@main.route('/changepwd/')
@login_required
def change_pwd():
    return render_template('changepwd.html')


class GradeApi(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('grade_name', type=str, required=True,
                                   help='请输入正确的班级名~')

    def get(self):
        g_id = request.args.get('g_id')
        if g_id:
            grade = Grade.query.get(g_id)
            return {
                'code': 200,
                'grade': grade.to_dict()
            }
        grades = Grade.query.all()
        return {
            'code': 200,
            'msg': '查询成功~',
            'grades': [grade.to_dict() for grade in grades]
        }

    def post(self):
        args = self.reqparse.parse_args()
        g_name = args.get('grade_name')
        if Grade.query.filter_by(g_name=g_name).first():
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
        g_id = request.form.get('g_id')
        g = Grade.query.get(g_id)
        db.session.delete(g)
        db.session.commit()
        return status_code.SUCCESS

    def patch(self):
        g_name = request.form.get('grade_name')
        g_id = request.form.get('g_id')
        g = Grade.query.get(g_id)
        g.g_name = g_name
        db.session.add(g)
        db.session.commit()
        return status_code.SUCCESS


class StudentApi(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('s_name', type=str, required=True,
                                   help='请输入正确的学生名~')
        self.reqparse.add_argument('gender', type=int, required=True,
                                   help='请输入正确的性别~')
        self.reqparse.add_argument('grade', type=int, required=True,
                                   help='请输入正确的班级名~')

    def get(self):
        s_id = request.args.get('s_id')
        if s_id:
            student = Student.query.get(s_id)
            return {
                'code': 200,
                'student': student.to_dict()
            }
        students = Student.query.all()
        return {
            'code': 200,
            'msg': '查询成功~',
            'students': [student.to_dict() for student in students]
        }

    def post(self):
        args = self.reqparse.parse_args()
        s_name = args.get('s_name')
        gender = args.get('gender')
        grade_id = args.get('grade')
        stu = Student()
        stu.s_name = s_name
        stu.gender = gender
        stu.grade_id = grade_id
        try:
            db.session.add(stu)
            db.session.commit()
        except Exception as e:
            return status_code.DATABASE_ERROR
        return {
            'code': status_code.OK,
            'msg': '添加学生信息成功~',
            'stu': stu.to_dict()
        }

    def delete(self):
        s_id = request.form.get('s_id')
        stu = Student.query.get(s_id)
        # db.session.delete(stu)
        # db.session.commit()
        return status_code.SUCCESS

    def patch(self):
        s_id = request.form.get('s_id')
        args = self.reqparse.parse_args()
        s_name = args.get('s_name')
        gender = args.get('gender')
        grade_id = args.get('grade')
        stu = Student.query.get(s_id)
        stu.s_name = s_name
        stu.gender = gender
        stu.grade_id = grade_id
        try:
            db.session.add(stu)
            db.session.commit()
        except Exception as e:
            return status_code.DATABASE_ERROR
        return {
            'code': status_code.OK,
            'msg': '修改学生信息成功~',
            'stu': stu.to_dict()
        }


api.add_resource(GradeApi, '/api/grade/', '/api/grade/<int:id>')
api.add_resource(StudentApi, '/api/student/', '/api/student/<int:id>')
