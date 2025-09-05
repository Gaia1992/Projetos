import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message_category = 'warning'

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'troque_esta_chave_segura')
    db_path = os.path.join(os.path.dirname(__file__), '..', 'db.sqlite3')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.abspath(db_path).replace('\\\\', '/')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    login_manager.init_app(app)

    from .models import User  # noqa
    from .routes import main_bp
    from .auth import auth_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)

    with app.app_context():
        db.create_all()

    return app
