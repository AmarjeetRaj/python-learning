class Account:
    def __init__(self):
        self._balance = 0
    @property
    def balance(self):
        return self._balance
    
    def deposit(self, amt):
        self._balance += amt
    
    def withdraw(self, amt):
        self._balance -= amt

def main():
    account = Account()
    print("Balance: ", account.balance)

    account.deposit(100)
    account.withdraw(50)

    print("Balance: ", account.balance)

if __name__=="__main__":
    main()