
class BankAccount:
    def __init__(self, account_holder_name, account_number, account_balance):
        self.account_holder_name = account_holder_name
        self.account_number = account_number
        self.account_balance = account_balance

    def display(self):
        print("Account Holder Name:", self.account_holder_name)
        print("Account Number:", self.account_number)
        print("Account Balance:", self.account_balance)

account = BankAccount("Madeeha", 123456789, 5000)
account.display()
