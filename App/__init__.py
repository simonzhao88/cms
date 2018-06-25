from flask import Flask

from App.exts_init import ext_init
from config import config, Config


def create_app(development):
    app = Flask(__name__,
                template_folder=Config.TEMPLATES_DIR,
                static_folder=Config.STATIC_DIR)

    app.config.from_object(config[development])
    config[development].init_app(app)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from .roles import role as role_blueprint
    app.register_blueprint(role_blueprint)
    ext_init(app)
    return app
