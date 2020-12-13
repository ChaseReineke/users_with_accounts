class User:
    def __init__(self, username_from_user="placeholder_username", email_from_user="placeholder@email.net", password_from_user="placeholder_password"):
        self.username = username_from_user        
        self.email = email_from_user
        self.password = password_from_user
        
class BankAccountOne:
    def __init__(self, username_from_bankaccount_one='placeholder_username', balance_from_bankaccount_one=0, int_rate_from_bankaccount_one='1.01'):
        self.username1 = username_from_bankaccount_one
        self.balance1 = balance_from_bankaccount_one
        self.int_rate1 = int_rate_from_bankaccount_one
        
    def make_deposit1(self, amount):
        self.balance1 += amount
        return self
    def make_withdrawal1(self, amount):
        if amount > self.balance1:
            print("Insufficient funds.")
            self.balance1 -= 5
            self.display_user_balance1()
            return self
        else:
            self.balance1 -= amount
            return self
    def display_user_balance1(self):
        print(f"{self.username1}'s account balance: ${self.balance1}.")
        return self
    
drake = BankAccountOne("Drake1", 1000)
jay = BankAccountOne("Jay-Z1", 1000)
wayne = BankAccountOne("Lil Wayne1", 1000)

drake.make_withdrawal1(200).display_user_balance1()

class BankAccountTwo:
    def __init__(self, username_from_bankaccount_two='placeholder_username', balance_from_bankaccount_two=0, int_rate_from_bankaccount_two='1.01'):
        self.username2 = username_from_bankaccount_two
        self.balance2 = balance_from_bankaccount_two
        self.int_rate2 = int_rate_from_bankaccount_two
    
    def make_deposit2(self, amount):
            self.balance2 += amount
            return self
    def make_withdrawal2(self, amount):
        if amount > self.balance2:
            print("Insufficient funds.")
            self.balance2 -= 5
            self.display_user_balance2()
            return self
        else:
            self.balance2 -= amount
            return self
    def display_user_balance2(self):
        print(f"{self.username2}'s account balance: ${self.balance2}.")
        return self



drake = BankAccountTwo("Drake2", 2000)
jay = BankAccountTwo("Jay-Z2", 2000)
wayne = BankAccountTwo("Lil Wayne2", 2000)

drake.make_deposit2(1000).display_user_balance2()
