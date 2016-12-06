#!/usr/bin/env python

import os

from flask_script import Manager, Server
from flask_script.commands import ShowUrls, Clean
from bubblebooking import create_app
from bubblebooking.models import db, User

# default to dev config because no one should use this in
# production anyway
env = os.environ.get('BUBBLEBOOKING_ENV', 'dev')
app = create_app('bubblebooking.settings.%sConfig' % env.capitalize())

manager = Manager(app)
manager.add_command("server", Server())
manager.add_command("show-urls", ShowUrls())
manager.add_command("clean", Clean())


@manager.shell
def make_shell_context():
    """Create a python REPL with several default imports in the context of the app."""

    return dict(app=app, db=db, User=User)

@manager.command
def createdb():
    """Create a database with all tables of SQLAlchemy models."""
    db.create_all()


if __name__ == "__main__":
    manager.run()
