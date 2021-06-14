from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap

def create_app(config_name)

# initializing application
    app = Flask(__name__)

    # creating app configurations
    app.config.from_object(config_options[config_name])

    # initializing flask extensions
    bootstrap = Bootstrap(app)
    
    return app