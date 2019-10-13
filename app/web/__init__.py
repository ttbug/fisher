from flask import Blueprint

web = Blueprint('web', __name__)

# 这里必须导入该蓝图下所有的模块，新增模块时必须在此处导入
from app.web import book