# defined a function
def greet(name):
    print("Welcome " + name)
    print("Have a nice day!")

#greet("Tom Holland")
#greet("Andrew Garfield")
#greet("Henry Cavil")

def user(name, age, gender="male"):
    print(f"{name} is {age} yr old {gender}")

# positional arguments
user("tom", 27, "male")
# keyword argument
user(age=33, gender="male", name="peter")
# default argument
user("jon", 41)


# return value
def add(a, b, c):
    return a + b + c

result = add(26, 89, 22)
print(result)












