from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user
from .forms import LoginForm
from .models import User
from . import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data.strip()).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash('Login realizado com sucesso.', 'success')
            next_url = request.args.get('next') or url_for('main.dashboard')
            return redirect(next_url)
        flash('Usuário ou senha inválidos.', 'danger')
    return render_template('login.html', form=form)

@auth_bp.route('/logout')
def logout():
    if current_user.is_authenticated:
        logout_user()
        flash('Sessão encerrada.', 'info')
    return redirect(url_for('auth.login'))
