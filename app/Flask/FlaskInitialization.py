from flask import Flask
from app.Routes.deepFaceRoutes import bp as api_bp  # Import the blueprint

def create_app():
    app = Flask(__name__)

    app.config['DEBUG'] = True

    app.register_blueprint(api_bp)

    return app
