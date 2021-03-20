from flask import Flask
from app.views.process_payment import pp_blueprint
from app.config import configs


def create_app():
	"""Intialize flask app."""
	app = Flask(__name__)
	app.config.from_object(configs)
	register_blueprints(app)
	return app


def register_blueprints(app):
	"""Register Flask blueprints."""
	app.register_blueprint(pp_blueprint)


app = create_app()
app.run()
