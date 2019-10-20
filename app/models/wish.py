from .base import db, Base

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, SmallInteger
from sqlalchemy.orm import relationship


# 心愿清单模型
class Wish(Base):
    id = Column(Integer, primary_key=True)
    # 和用户关联
    user = relationship("User")
    uid = Column(Integer, ForeignKey('user.id'))
    # 和书籍关联
    isbn = Column(String(15), nullable=False)
    # 由于数据库中没有存储书籍的信息，这里不使用这种方法
    # book = relationship("Book")
    # bid = Column(Integer, ForeignKey('book.id'))
    # 表示书籍是否送出
    launched = Column(Boolean, default=False)
    