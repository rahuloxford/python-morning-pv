
# local variables: can only be used inside the function they are created.
# global variables: can be used in any function, anywhere in the code.


j = 49 # global variable: can be used anywhere, inside or outside the functions.

def demo():
    a = 15 # local variable: can only be used in this function
    print(a)
    print(j)

demo()
# print(a) # will give error as the variable a is local
print(j)
