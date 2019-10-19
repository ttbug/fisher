from flask import Flask
from app.models.book import db
from flask_login import LoginManager

login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.settings')

    register_blueprint(app)

    db.init_app(app)
    login_manager.init_app(app)
    # 告诉flask，登陆页面视图函数是什么
    login_manager.login_view = 'web.login'
    login_manager.login_message = "请先登陆或注册"
    # 查看源码，这里的问题可以有三种解决方法，传入app
    db.create_all(app=app)

    # with app.app_context():
    #     db.create_all()
        
    return app

# 把蓝图注册到app
def register_blueprint(app):
    from app.web import web
    app.register_blueprint(web)