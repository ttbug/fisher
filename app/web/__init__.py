from flask import Blueprint

# web = Blueprint('web', __name__, template_folder="templates")
web = Blueprint('web', __name__)

# 这里必须导入该蓝图下所有的模块，新增模块时必须在此处导入
from app.web import book
from app.web import auth
from app.web import main
from app.web import drift
from app.web import gift
from app.web import wish