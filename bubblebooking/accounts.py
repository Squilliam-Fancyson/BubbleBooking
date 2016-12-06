

class Account(object):

    def __init(self, acct_name, acct_id, acct_password):
        #account name, account number, password
        self.acctName = acct_name
        self.acctNum = acct_id
        self.password = acct_password
        self.permissions = Permissions("regular")

class Admin(Account):
    def __init(self):
        self.permissions = Permissions("admin")

    #ban and unban users
    def banUser(self, acct_id):
        self.permissions.permissions.isBanned = True

    def unbanUser(self, acct_id):
        self.permissions.permissions.isBanned = False

    def modifyPermissions(self, accountId, permissionKey, permissionValue):
        accountId.permissionKey = permissionValue

class Faculty(Account):

    def __init(self):
        self.permissions = Permissions("faculty")

    def overrideEvent(self, eventId):
        #todo

class Permissions(self, accountType):
    if accountType = faculty:
        permissions = {'isBanned': False, 'createEvent': True, 'deleteOwnEvent': True, 'deleteOtherEvent': True, ' banUser': False,
                       'unbanUser': False, 'overrideFaculty': False, 'overrideStudent': True}

    else if accountType = admin:
        permissions = {'isBanned': False, 'createEvent': True, 'deleteOwnEvent': True, 'deleteOtherEvent': True, ' banUser': True,
                       'unbanUser': True, 'overrideFaculty': True, 'overrideStudent': True}

    else:
        permissions = {'isBanned': False, 'createEvent': True, 'deleteOwnEvent': True, 'deleteOtherEvent': False, ' banUser': False,
                        'unbanUser': False, 'overrideFaculty': False, 'overrideStudent': False}

    modifyPermissions(permissionKey, value):
        permissionKey = value