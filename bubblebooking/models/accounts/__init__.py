#!/usr/bin/env python3
from flask_login import AnonymousUserMixin
from flask_login import UserMixin
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash

from bubblebooking.models import db
from bubblebooking.models.accounts.permissions import Permissions


class Account(db.Model, UserMixin):
    username = db.Column(db.String(), primary_key=True)
    credential = db.Column(db.String())
    acc_type = db.Column("type", db.Enum("regular", "faculty", "admin",
                                 name="AccountTypeEnum"))

    permissions = Permissions(acc_type)

    def __init__(self, username, credential):
        self.username = username
        self.set_credential(credential)

    def set_credential(self, password):
        self.credential = generate_password_hash(password)

    def check_credential(self, value):
        check_password_hash(self.credential, value)

    @property
    def is_authenticated(self):
        if isinstance(self, AnonymousUserMixin):
            return False
        else:
            return True

    def is_active(self):
        return True

    def is_anonymous(self):
        if isinstance(self, AnonymousUserMixin):
            return True
        else:
            return False

    def get_username(self):
        return self.username

    def __repr__(self):
        return "<User {name}>".format(self.username)
