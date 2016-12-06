from flask_sqlalchemy import Model

from bubblebooking.models import db


class Permissions(db.Model):
   """Default Permissions"""

    self.permissions = db.Column(db.PickleType({
            "is_banned": False,
            "create_event": False,
            "delete_own_event": False,
            "delete_other_event": False,
            "ban_user": False,
            "unban_user": False,
            "override_faculty": False,
            "override_student": False
        }))

    def __init__(self, acc_type):

        """Update Permissions for Each Account Type"""
        if acc_type == "regular":
            self.permissions.update(
                create_event=True,
                delete_own_event=True
            )
        elif acc_type == "faculty":
            self.permissions.update(
                create_event=True,
                delete_own_event=True,
                override_student=True
            )
        elif acc_type == "admin":
            self.permissions.update(
                create_event=True,
                delete_own_event=True,
                delete_other_event=True,
                ban_user=True,
                unban_user=True,
                override_faculty=True,
                override_student=True
            )


    def modify_permission(self, prm_key: str, value: bool):
         """Modify Permission for Specified Account Name, Permission Type, and Permission Value"""
        self.permissions[prm_key] = value

    def has_permission(self, prm_key) -> bool:
        """Determines if an Account has the required permissions"""
        return self.permissions[prm_key]
