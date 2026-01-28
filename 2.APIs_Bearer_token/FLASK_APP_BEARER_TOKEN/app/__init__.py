from flask import Flask 
from .config import Config
from .extensions import jwt

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    jwt.init_app(app)

    from .auth.routes import auth_bp
    from .users.routes import user_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(user_bp)

    return app