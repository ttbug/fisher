from .base import db, Base
from sqlalchemy import Column, Integer, String, Boolean, Float
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login_manager

from app.libs.helper import is_isbn_or_key
from app.spider.fisher_book import FisherBook
from app.models.gift import Gift
from app.models.wish import Wish

class User(Base, UserMixin):
    id = Column(Integer, primary_key=True)
    nickname = Column(String(24), nullable=False)
    phone_number = Column(String(18), unique=True)
    email = Column(String(50), unique=True, nullable=False)
    _password = Column('password', String(128), nullable=False)
    confirmed = Column(Boolean, default=False)
    beans = Column(Float, default=0)
    send_counter = Column(Integer, default=0)
    receive_counter = Column(Integer, default=0)
    wx_open_id = Column(String(50))
    wx_name = Column(String(32))

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    def check_password(self, raw):
        return check_password_hash(self._password, raw)

    # login_user函数要求，必须定义这个函数，如果不是id的话，需要覆盖这个函数
    # def get_id(self):
    #     return self.id

    def can_save_to_list(self, isbn):
        if is_isbn_or_key(isbn) != 'isbn':
            return False
        
        fisher_book = FisherBook()
        fisher_book.search_by_isbn(isbn)
        #　查询系统是否存在这本书
        if not fisher_book.first:
            return False

        # 不允许一个用户同时赠送多本相同的书
        # 一个用户不能同时成为同一本书的赠送者和索要者
        gifting = Gift.query.filter_by(uid=self.id, isbn=isbn,
                                       launched=False).first()
        wishing = Wish.query.filter_by(uid=self.id, isbn=isbn,
                                        launched=False).first()

        if not wishing and not gifting:
            return True
        else:
            return False

# 需要被flask_login 调用的
@login_manager.user_loader
def get_user(uid):
    return User.query.get(int(uid))