OK = 200
DATABASE_ERROR = {'code': 0, 'msg': '数据库错误，稍后重试~'}
SUCCESS = {'code': 200, 'msg': '请求成功～'}

# 用户模块
USER_REGISTER_NOT_NULL = {'code': 1001, 'msg': '请填写完所有参数~'}
USER_REGISTER_MOBILE_ERROR = {'code': 1002, 'msg': '请输入正确的手机号~'}
USER_REGISTER_PASSWORD_IS_NOT_VALID = {'code': 1003, 'msg': '两次输入密码不一致~'}
USER_REGISTER_EXITS_USER = {'code': 1004, 'msg': '该用户已注册，请直接登录~'}


USER_LOGIN_NOT_NULL = {'code': 1005, 'msg': '请填写完所有参数~'}
USER_LOGIN_MOBILE_ERROE = {'code': 1006, 'msg': '用户不存在，请先注册~'}
USER_LOGIN_PASSWORD_ERROE = {'code': 1007, 'msg': '用户名或密码错误~'}


USER_CHANGE_PROFILE_IMAGES_ERROR = {'code': 1008, 'msg': '上传图片格式错误~'}
USER_CHANGE_PROFILE_NAME_ERROR = {'code': 1009, 'msg': '用户名已存在，请重新设置~'}

# 班级模块
GRADE_ADD_EXITS_ERROR = {'code': 2001, 'msg': '班级已经存在~'}