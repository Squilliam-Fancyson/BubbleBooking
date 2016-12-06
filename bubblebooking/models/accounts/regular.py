from bubblebooking.models.accounts import Account
from bubblebooking.models.accounts import Permissions

class RegularAccount(Account):
    def __init__(self):
        self.acc_type = "regular"
        self.permissions = Permissions("regular")
