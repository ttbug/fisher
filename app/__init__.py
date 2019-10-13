from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    register_blueprint(app)
    return app

# 把蓝图注册到app
def register_blueprint(app):
    from app.web import web
    app.register_blueprint(web)