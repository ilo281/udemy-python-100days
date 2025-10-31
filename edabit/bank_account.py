"""
Bank Account

In this project, we’ll create a Python class that can be used to create and manipulate a personal bank account.

The bank account class you’ll create should have methods for each of the following:

    Accepting deposits
    Allowing withdrawals
    Showing the balance
    Showing the details of the account

Note: As with professional software development, you should be saving your code very often. As you code, make sure you click the “Save” button below to save your code/changes. Otherwise, you run the risk of losing all your code!

Let’s begin!

"""
class BankAccount:
    balance = 100
    show_name = "Bank of Russia"
    def accept_deposit(self, input_money):
        self.balance = self.balance + input_money
    def allowing_withdraw(self, deduct_money):
        self.balance = self.balance - deduct_money
    def display_balance(self):
        show_balance = self.balance
        return show_balance
    def display_details(self):
        show_name = "Bank of America " + self.show_name
        return show_name


if __name__ == "__main__":

    bank_account_object = BankAccount()
    print("current balance", bank_account_object.display_balance())
    bank_account_object.accept_deposit(60)
    print("current balance", bank_account_object.display_balance())
    bank_account_object.allowing_withdraw(1)
    print("current balance", bank_account_object.display_balance())
    print(bank_account_object.display_details())
