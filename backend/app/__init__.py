from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_cors import CORS
from flask_login import LoginManager
from flask_mail import Mail
from app.config import Config



db = SQLAlchemy()
bcrypt = Bcrypt()
migrate = Migrate()
mail = Mail()



def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app, supports_credentials=True)


    db.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)

    from app.auth.models import User
    from app.auth.routes import auth
    from app.user.routes import user
    from app.posts.routes import post

    app.register_blueprint(auth, url_prefix='/auth/')
    app.register_blueprint(user, url_prefix='/user/')
    app.register_blueprint(post, url_prefix='/post/')

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)


    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    return app