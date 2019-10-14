from flask import Flask
from app.models.book import db

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.settings')

    register_blueprint(app)

    db.init_app(app)
    # 查看源码，这里的问题可以有三种解决方法，传入app
    db.create_all(app=app)

    # with app.app_context():
    #     db.create_all()
        
    return app

# 把蓝图注册到app
def register_blueprint(app):
    from app.web import web
    app.register_blueprint(web)