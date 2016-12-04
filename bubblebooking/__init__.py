#!/usr/bin/env python3
"""Bubble Booking scheduling system.

A scheduling system for students and faculty to reserve rooms in a building
of a given organization. Runs on the flask microframework.

Example:
    This application can be started through the manage.py script::

        $ ./manage.py server

    Once started, you can access the home page through any browser on
    ``http://127.0.0.1:5000/``.

Note:
    This application requires Python 3.3+.

"""

__author__ = 'Squilliam Fancyson'
__version__ = '0.1'  # TODO: change with every version change.

from flask import Flask
from webassets.loaders import PythonLoader as PythonAssetsLoader

from bubblebooking.views.main import main
from bubblebooking import assets
from bubblebooking.models import db

from bubblebooking.extensions import (
    cache,
    assets_env,
    debug_toolbar,
    login_manager
)


def create_app(object_name):
    """Creates a flask application with a factory.

    More details are explained here:
    http://flask.pocoo.org/docs/patterns/appfactories/

    Arguments:
        object_name (str): the python path of the config object.
            e.g. bubblebooking.settings.ProdConfig

        env (str): The name of the current environment.
            e.g. prod or dev

    Returns:
        Flask: The produced flask application.

    """

    app = Flask(__name__)

    app.config.from_object(object_name)

    # initialize the cache
    cache.init_app(app)

    # initialize the debug tool bar
    debug_toolbar.init_app(app)

    # initialize SQLAlchemy
    db.init_app(app)

    login_manager.init_app(app)

    # Import and register the different asset bundles
    assets_env.init_app(app)
    assets_loader = PythonAssetsLoader(assets)
    for name, bundle in assets_loader.load_bundles().items():
        assets_env.register(name, bundle)

    # register our blueprints
    app.register_blueprint(main)

    return app
