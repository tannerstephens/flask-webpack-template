from flask import Flask
from tricky_treats.routes import pages

def create_app(config_object='tricky_treats.settings'):
  app = Flask(__name__.split('.')[0])
  app.config.from_object(config_object)
  register_extensions(app)
  app.register_blueprint(pages)

  return app


def register_extensions(app):

  return None
