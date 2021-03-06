from bubblebooking.models.accounts import Account
from bubblebooking.models.accounts import Permissions

class FacultyAccount(Account):
    def __init__(self):
        """Inherit from Account Class"""
        super().__init__()
        self.acc_type = "faculty"
        self.permissions = Permissions("faculty")
