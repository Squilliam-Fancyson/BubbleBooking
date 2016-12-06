"""Controller for the Permission model."""

from bubblebooking.models.permission import Permission
from bubblebooking.models.accounts.admin import AdminAccount


class PermissionController(object):
    """Controls the permissions of a user account.

    This controller is used by the AdminAccount model to modify privileges the Account model.

    Methods:
        verify_permissions (bool): Verifies that an Account instance has a required permission.
    
        grant_permission: Adds a specified permission to an Account instance.
    
    """
    
    def verify_permissions(self, user_perms: Permission, perm: str) -> bool:
        """Verifies if a user has the specified permission.
        
        Args:
            user_perms (Permission): Permissions of a user.
            
            perm (str): Permission to verify.
        
        """
        return user_perms.has_permission(perm)
    
    def grant_permission(self, admin_perms: Permission, user_perms: Permission, perm: str):
        """Grants a permission to a user.
        
        Args:
            admin_perms (AdminAccount): Permissions of the modifying user -- presumably 
                an administrator.
            
            user_perms (Permission): Permissions of the user to modify.
            
            perm (str): Permission to grant.
        
        """
        if admin_perms.has_permission("canModifyPermissions"):
            user_perms.modify_permission(perm)
