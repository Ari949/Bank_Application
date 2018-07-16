
class BankAccount:

    acount = []

    def __init__(self, person_id, first_name, last_name, password, amount_of_money=0):
        self.person_id = person_id
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.amount_of_money = amount_of_money

    def __str__(self):
        user = "person_id:%s\n first_name:%s \n last_name:%s \n password: %s amount_of_money %d" % (self.person_id, self.first_name, self.last_name, self.password, self.amount_of_money)
        BankAccount.acount.append(user)
        return user

    # def create_account(self):

    def get_person_id(self):
        return self.person_id

    def add(self, money):
        if money < 0:
            print ("Negative money")
            return
        self.amount_of_money += money

    def sub(self, money):
        if money < 0:
            print ("Negative money")
            return
        self.amount_of_money -= money

    def transfer(self, other, amount):
        other.add(amount)
        self.sub(amount)

    def login(self, person_id, password):

        if self.person_id != person_id or self.password != password:
            return False
        return True
