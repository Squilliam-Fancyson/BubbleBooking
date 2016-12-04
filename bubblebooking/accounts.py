

class Account(self, acct_name, acct_num):

    #account name, account number
    self.acctName = acct_name
    self.acctNum = acct_id

    #regular account default permissions
    perCreateEvent = True
    perDeleteEvent = True

    perBanUser = False
    perUnbanUser = False

    perOverrideFaculty = False
    perOverrideStudent = False

class Admin():

    perBanUser = True
    perUnbanUser = True

    perOverrideFaculty = True
    perOverrideStudent = True

    #ban and unban users
    def banUser(self, acct_id):
        #todo

    def unbanUser(self, acct_id):
        #todo


class Faculty():

    perOverrideStudent = True


