
# try:
#     print(peter)
# except NameError:
#     print("You must be using a variable which is'nt created")
# except ZeroDivisionError:
#     print("Division by zero is not allowed, dumbo")
# except:
#     print("Somethign went wrong")
# else:
#     print("program finished without error")
# finally:
#     print("program finished")


age = eval(input("What is your age? "))

if age >= 18:
    print("user can vote")
else:
    raise TypeError("You are just a kid")