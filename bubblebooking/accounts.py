

class Accounts(object):

    def __init__(self, credential, accountType, userName):
        #account name, account number, password
        self.credential = credential
        self.accountType = accountType
        self.userName = userName

    def modifyPermission(self):
        #todo

    def isOrganizer(self):
        #todo

    # ban and unban users
    def banUser(self, userName):
        if self.permissions.hasPermissions(userName) == True:
                userName.permissions.permissions.isBanned = True

    def unbanUser(self, userName):
        if self.permissions.hasPermissions(userName) == True:
            userName.permissions.permissions.isBanned = False


class Regular(Accounts):
    def __init__(self, acct_id):
        self.permissions = Permissions("regular")


class Admin(Accounts):
    def __init__(self):
        self.permissions = Permissions("admin")


class Faculty(Accounts):

    def __init__(self):
        self.permissions = Permissions("faculty")

    def overrideEvent(self, eventId):
        #todo

class Permissions(Accounts):

    def __init__(self):
        if self.accountType == "faculty":
            permissions = {'isBanned': False, 'createEvent': True, 'deleteOwnEvent': True, 'deleteOtherEvent': True, ' banUser': False,
                           'unbanUser': False, 'overrideFaculty': False, 'overrideStudent': True}

        if self.accountType == "admin":
            permissions = {'isBanned': False, 'createEvent': True, 'deleteOwnEvent': True, 'deleteOtherEvent': True, ' banUser': True,
                           'unbanUser': True, 'overrideFaculty': True, 'overrideStudent': True}

        else:
            permissions == {'isBanned': False, 'createEvent': True, 'deleteOwnEvent': True, 'deleteOtherEvent': False, ' banUser': False,
                            'unbanUser': False, 'overrideFaculty': False, 'overrideStudent': False}

    def modifyPermissions(self, userName, permissionKey, value):
            if self.permissions.hasPermissions(userName) == True:
                userName.permissions.permissions.permissionKey = value

    def hasPermissions(self, userName):
        #todo

