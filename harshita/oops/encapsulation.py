
class Atm:
    def __init__(self, accno, balance, pin):
        self.__accno = accno
        self.__balance = balance
        self.__pin = pin

    def deposit(self, amount):
        self.__balance += amount
        print("deposited successfully")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("withdrawl successful")
        else:
            print("insufficient balance")

    def show_balance(self):
        print(f"your current balance is: {self.__balance}")

sbi = Atm(65446469865, 1300, 4862)

# trick to change the private vars values
# sbi._Atm__balance = 200000

sbi.show_balance()
sbi.deposit(11000)

sbi.show_balance()
sbi.withdraw(1500)
sbi.show_balance()

sbi.deposit(14000)
sbi.show_balance()




