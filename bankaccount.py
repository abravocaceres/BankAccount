class BankAccount:
    def __init__(self, int_rate = 0.01, balance = 0):
        if int_rate is None:
            self.int_rate = 0.01
        else:
            self.int_rate = int_rate    
        if balance is None:
            self.balance = 0 
        else:
            self.balance = balance      

	 

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance <= 0:
            print("Fondos insuficientes: cobrar una tarifa de $ 5")
            tarifa = 5
            self.balance = self.balance - tarifa
        self.balance = self.balance - amount
        return self

    def display_account_info(self):
        print(self.balance)
        return self

    def yield_interest(self):
        if self.balance >= 0:
            porcentaje = self.balance * self.int_rate
            self.balance = self.balance + porcentaje
            
        return self



cuenta1 = BankAccount()
cuenta1.deposit(100).deposit(100).deposit(100).withdraw(20).yield_interest().display_account_info()

cuenta2 = BankAccount()
cuenta2.deposit(1000).deposit(5000).withdraw(500).withdraw(20).withdraw(50).withdraw(60).withdraw(60).yield_interest().display_account_info()



# cuenta2 = BankAccount()
# cuenta1.deposit(1000)
# cuenta1.yield_interest()
# cuenta1.display_account_info()