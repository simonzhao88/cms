from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class User(db.Model):
    u_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(24), unique=True, nullable=False)
    password_hash = db.Column(db.String(168), nullable=False)
    gender = db.Column(db.Boolean, default=True)
    email = db.Column(db.String(24))
    avatar = db.Column(db.String(168), default='/static/img/icons/avatar.png')
    phone = db.Column(db.String(15))

    @property
    def password(self):
        raise AttributeError('密码不可读~')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


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
