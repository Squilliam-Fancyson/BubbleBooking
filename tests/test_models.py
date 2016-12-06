#!/usr/bin/env python3

import pytest

from bubblebooking.models import db
from bubblebooking.models.accounts import Account
from bubblebooking.models.accounts.admin import AdminAccount


create_user = False


@pytest.mark.usefixtures("testapp")
class TestModels:
    def test_user_save(self, testapp):
        """ Test Saving the user model to the database """

        admin = AdminAccount("admin", "supersafepassword")
        db.session.add(admin)
        db.session.commit()

        user = Account.query.filter_by(username="admin").first()
        assert user is not None

    def test_user_password(self, testapp):
        """ Test password hashing and checking """

        admin = AdminAccount("admin", "supersafepassword")

        assert admin.username == 'admin'
        assert admin.check_password('supersafepassword')
