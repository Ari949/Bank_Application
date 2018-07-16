from bank_account import BankAccount
from bank import Bank
import os
account = []
accounts = []
clear = lambda: os.system('cls')

# def insert_to_file(account):
#     for item in account:


def choose_create_user(item):

        clear()
        if item == 0:
            print ("Please enter your person_id, first name, last name, password, amount of money")
            person_id, first_name, last_name, password, amount_of_money = raw_input().split(',')
            my_account = BankAccount(first_name, last_name, password, amount_of_money)
            account.append(my_account)
        # file_base = open("C::\\".join("Users"), 'w')
        file_base = open('C:\\Users\\ari\\Desktop\\Python\\Examples\\Ex1\\dataBase.txt', 'a')
        file_base.write("{0}".format(account[0]))
        # file_base.write('person_id:%s \n first name:%s\n last name:%s\n password:%s\n amount of money:%s\n' % (person_id, first_name, last_name, password, amount_of_money))
        file_base.close()

     # "{0}, {1}".format()
     # elif option ==1:
     #    import  socket







def main():

    # a = BankAccount('1', 'h', 'b', 'a', 5)
    # bank = Bank()

    option = input(" Hello, Insert 1 to Sign for your account Or 0 to create one")
    if option == 0:
        choose_create_user(option)
#comeback to this_______________________

    # elif option == 1:
    #         clear()
    #         User=bank
    #         first_name = BankAccount.first_name()
    #         screen = input('Hello ,%s \n' % first_name + 'To see your possible Actions Press 1.\n To see your Balance '
    #                                                      'press 0')
    #         if screen == 1:
    #            action = input("1.Transfer Money To other account press 1")
    #


               # bank.insert(a)
    # bank.insert(a)
    # print bank.get_account_by_id('1')
    # bank.remove('1')
    # bank.remove('1')


if __name__ == '__main__':
    main()
