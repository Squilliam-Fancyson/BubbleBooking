

class Account(self, acct_name, acct_num, password):

    #account name, account number, password
    self.acctName = acct_name
    self.acctNum = acct_id
    self.password = password

    #regular account default permissions
    #CONVERT PERMISSIONS TO STRUCT!!
    perCreateEvent = True
    perDeleteOwnEvent = True

    perDeleteOtherEvent = False

    perBanUser = False
    perUnbanUser = False

    perOverrideFaculty = False
    perOverrideStudent = False

class Admin():

    perDeleteOtherEvent = True

    perBanUser = True
    perUnbanUser = True

    perOverrideFaculty = True
    perOverrideStudent = True

    #ban and unban users
    def banUser(self, acct_id):
        #todo

    def unbanUser(self, acct_id):
        #todo

    def modifyPermissions(self, acct_id):
        #todo

class Faculty():

    #need to double check permissions
    perOverrideStudent = True
    perDeleteOtherEvent = True

