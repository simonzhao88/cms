from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


rp = db.Table('rp',
              db.Column('r_id', db.Integer, db.ForeignKey('roles.r_id'), primary_key=True),
              db.Column('p_id', db.Integer, db.ForeignKey('permission.p_id'), primary_key=True))


class Role(db.Model):
    __tablename__ = 'roles'
    r_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    r_name = db.Column(db.String(30), nullable=False)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def to_dict(self):
        return {
            'r_id': self.r_id,
            'r_name': self.r_name
        }


class User(db.Model):
    __tablename__ = 'user'
    u_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(24), unique=True, nullable=False)
    password_hash = db.Column(db.String(168), nullable=False)
    gender = db.Column(db.Boolean, default=True)
    email = db.Column(db.String(24))
    avatar = db.Column(db.String(168), default='/static/img/icons/avatar.png')
    phone = db.Column(db.String(15))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.r_id'))

    @property
    def password(self):
        raise AttributeError('密码不可读~')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        return {
            'u_id': self.u_id,
            'u_name': self.username,
            'role': self.role.r_name if self.role else '无'
        }


class Grade(db.Model):
    g_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    g_name = db.Column(db.String(24), nullable=False, unique=True)
    create_time = db.Column(db.DateTime, default=datetime.now)
    student = db.relationship('Student', backref='grade', lazy='dynamic')

    def to_dict(self):
        return {
            'g_id': self.g_id,
            'g_name': self.g_name,
            'create_time': self.create_time.strftime('%Y-%m-%d')
        }


class Student(db.Model):
    s_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    s_name = db.Column(db.String(24), nullable=False)
    gender = db.Column(db.Boolean, default=True)
    grade_id = db.Column(db.Integer, db.ForeignKey('grade.g_id'))

    def to_dict(self):
        return {
            's_id': self.s_id,
            's_name': self.s_name,
            'gender': self.gender,
            'grade_id': self.grade_id,
            'grade_name': self.grade.g_name
        }


class Permission(db.Model):
    __tablename__ = 'permission'
    p_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    p_name = db.Column(db.String(30), nullable=False)
    roles = db.relationship('Role', secondary=rp, backref='permission', lazy='dynamic')

    def to_dict(self):
        return {
            'p_id': self.p_id,
            'p_name': self.p_name
        }