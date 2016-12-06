from flask_wtf import Form
from wtforms import PasswordField
from wtforms import StringField
from wtforms import validators

from bubblebooking.models import Account


class LoginForm(Form):
    username = StringField("Username", validators=[validators.required()])
    credential = PasswordField("Password", validators=[validators.optional()])

    def validate(self):
        check_validate = super().validate()

        # Basic form validation.
        if not check_validate:
            return False

        # Existence of user account.
        user = Account.query.filter_by(username=self.username.data).first()
        if not user:
            self.username.errors.append('Invalid username or password')
            return False

        # Correct account credentials.
        if not user.check_password(self.password.data):
            self.credential.errors.append('Invalid username or password')
            return False

        return True

class BestFitCriteriaForm(self):
    pass
