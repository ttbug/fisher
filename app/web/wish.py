from . import web

from app import db

from flask import current_app, redirect, url_for, flash
from flask_login import current_user, login_required
from app.models.gift import Gift
from app.models.wish import Wish

@web.route('/book/my_wish')
def my_wish():
    pass

@web.route('/wish/book/<isbn>')
@login_required
def save_to_wish(isbn):
    if current_user.can_save_to_list(isbn):
        # 事务
        # rollback
        with db.auto_commit():
            wish = Wish()
            wish.isbn = isbn
            # current_user和get_user有关系
            wish.uid = current_user.id
            db.session.add(wish)
    else:
        flash("这本书已经添加到您的赠送清单或已存在于您的心愿清单，请不要重复添加")

    return redirect(url_for('web.book_detail', isbn=isbn))


@web.route('/satisfy/wish/<int:wid>')
def satisfy_wish(wid):
    pass