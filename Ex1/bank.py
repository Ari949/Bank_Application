class Bank:
    def __init__(self):
        self.accounts = {}

    def insert(self, account):
        if self.accounts.has_key(account.get_person_id()):
            print ("Account exists")
            return False


        self.accounts[account.get_person_id()] = account

    def remove(self, person_id):
        if not self.accounts.has_key(person_id):
            print ("Account does not exist")
            return False

        self.accounts.pop(person_id)
        return True

    def get_account_by_id(self, person_id):
        if not self.accounts.has_key(person_id):
            print ("Account does not exist")
            return False

        return self.accounts[person_id]