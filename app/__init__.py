import os

from flask import Flask
from flask_migrate import Migrate

from app.models import db
from app.routes.department import department_bp
from app.routes.employee import employee_bp
from app.routes.home import home_bp
from config import Config

migrate = Migrate()


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
        "DATABASE_URL",
        app.config.get("SQLALCHEMY_DATABASE_URI", "sqlite:///employee.db"),
    )

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(home_bp)
    app.register_blueprint(employee_bp)
    app.register_blueprint(department_bp)

    with app.app_context():
        db.create_all()

    return app