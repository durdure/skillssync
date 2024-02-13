from flask import Flask, session, jsonify
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
    from app.mentor.routes import mentor
    from app.posts.routes import post
    from app.mentor.models import Mentor
    from app.routes import test



    app.register_blueprint(auth, url_prefix='/auth/')
    app.register_blueprint(user, url_prefix='/user/')
    app.register_blueprint(mentor, url_prefix='/mentor/')
    app.register_blueprint(post, url_prefix='/post/')
    app.register_blueprint(test)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)


    @login_manager.user_loader
    def load_user(user_id):
        # Check if the user ID corresponds to a Mentor
        mentor = Mentor.query.get(user_id)
        if mentor:
            return mentor

        # If the user ID does not correspond to a Mentor, return a User
        return User.query.get(int(user_id))
    
    @login_manager.unauthorized_handler
    def unauthorized():
        return jsonify({'error': 'Unauthorized', 'message': 'You must be logged in to access this resource'}), 401

    
    return app