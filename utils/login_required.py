from functools import wraps

from flask import session, redirect, url_for


def login_required(f):
    """
    登录验证装饰器
    :param f:
    :return:
    """
    @wraps(f)
    def check_login(*args, **kwargs):
        u_id = session.get('u_id')
        if not u_id:
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return check_login
