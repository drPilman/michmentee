from flask import Flask, render_template, request, redirect, flash, url_for
from flask_login import login_user, login_required, current_user, logout_user
from flask import Blueprint
from . import db
from .models import *
import bcrypt

auth = Blueprint('auth', __name__)


@auth.route('/signup')
def signup():
    return render_template('registration.html')


@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    full_name = request.form.get('full_name')
    password = request.form.get('password')
    password2 = request.form.get('password2')
    surname = request.form.get('surname')
    name = request.form.get('name')
    patronymic = request.form.get('patronymic')
    birthday = request.form.get('birthday')
    study = request.form.get('study')
    number = request.form.get('number')
    faculty = request.form.get('faculty')

    if email and email.islower() and email.isascii(
    ) and password and password.isascii():
        email = email.strip()
        if password2 == password:
            if db.session.query(Users).filter(
                    Users.email == email).one_or_none() is None:
                hashAndSalt = bcrypt.hashpw(password.encode('utf-8'),
                                            bcrypt.gensalt())
                db.session.add(
                    Users(email=email,
                          surname=surname,
                          name=name,
                          patronymic=patronymic,
                          birthday=birthday,
                          study=study,
                          number=number,
                          faculty=faculty,
                          password_hash=hashAndSalt))
                db.session.commit()
                return redirect(url_for('main.index'))
            else:
                flash("Пользователь с таким ником уже зарегистрирован")
        else:
            flash("Пароли не совпадают")
    else:
        flash("Некорректные логин или пароль")
    return redirect(url_for('auth.signup'))


@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    if email and email.islower() and email.isascii(
    ) and password and password.isascii():
        email = email.strip()
        if (user := db.session.query(Users).filter(
                Users.email == email).one_or_none()):
            if (bcrypt.checkpw(password.encode('utf-8'), user.password_hash)):
                login_user(user)
                return redirect(url_for('main.profile'))

    flash("Некорректные логин или пароль")
    return redirect(url_for('auth.login'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
