from . import web
from app.models.base import db
from app.forms.auth import RegisterForm, LoginForm
from app.models.user import User

from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user

@web.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        with db.auto_commit():
            user = User()
            user.set_attrs(form.data)
            db.session.add(user)
        return redirect(url_for('web.login'))

    return render_template('auth/register.html', form=form)


@web.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            next = request.args.get('next')
            if not next or not next.startswith('/'):
                next = url_for('web.index')
            return redirect(next)
        else:
            flash("账号不存在或密码错误")
    return render_template('auth/login.html', form=form)

@web.route('/reset/password', methods=['GET', 'POST'])
def forget_password_request():
    pass

@web.route('/reset/password/<token>', methods=['GET', 'POST'])
def reset_password_request(token):
    pass