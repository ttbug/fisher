from . import web
from flask_login import login_required, current_user
from app.models.gift import Gift
from flask import current_app, flash, redirect, url_for

from app import db

@web.route('/my/gifts')
@login_required
def my_gifts():
    pass

@web.route('/gifts/book/<isbn>')
@login_required
def save_to_gifts(isbn):
    if current_user.can_save_to_list(isbn):
        # 事务
        # rollback
        with db.auto_commit():
            gift = Gift()
            gift.isbn = isbn
            # current_user和get_user有关系
            gift.uid = current_user.id
            current_user.beans += current_app.config['BEANS_UPLOAD_ONE_BOOK']
            db.session.add(gift)
    else:
        flash("这本书已经添加到您的赠送清单或已存在于您的心愿清单，请不要重复添加")

    return redirect(url_for('web.book_detail', isbn=isbn))

@web.route('/gifts/<gid>/redraw')
def redraw_from_gifts(gid):
    pass