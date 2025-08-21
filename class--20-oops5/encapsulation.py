# encapsulation: hiding data.

class Atm:
    def __init__(self, accno, balance, pin):
        self.__accno = accno
        self.__balance = balance
        self.__pin = pin

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance")
        else:
            p = eval(input("Enter your pin: "))
            if p == self.__pin:
                self.__balance -= amount
                print("Withdrawl Successful")
            else:
                print("Wrong pin entered")

    def deposit(self, amount):
        self.__balance += amount
        print("Deposit Successful")

    def show_balance(self):
        print("Your balance is:", self.__balance)

    def change_pin(self):
        old_pin = eval(input("Enter your old pin: "))
        if old_pin == self.__pin:
            new_pin = eval(input("Enter your new pin: "))
            self.__pin = new_pin
            print("Pin changed successfully")
        else:
            print("Wrong old pin")
            print("Cannot change the pin")


sbi = Atm(594478876987, 12000, 1487)
