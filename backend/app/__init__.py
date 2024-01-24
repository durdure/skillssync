from flask import Flask, session
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_cors import CORS
from flask_login import LoginManager

db = SQLAlchemy()
bcrypt = Bcrypt()
migrate = Migrate()



def create_app(config=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app, supports_credentials=True)


    db.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)

    from app.auth.models import User
    from app.auth.routes import auth

    app.register_blueprint(auth, url_prefix='/auth/')

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)


    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    return app