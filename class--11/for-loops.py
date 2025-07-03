
# Q. print "Hello World" 10 times

for i in range(1, 11):
    print("Hello World", i)

# Q. print all the elements from 10 to 50

for i in range(10, 51):
    print(i)

# Q. print all the names from the list

names = ['lewis hamilton', 'max verstappen', 'charles leclerc']

for name in names:
    print(name)

# Q. print table of a number (by the user)

num = int(input('enter a number to get the table? '))

for i in range(1, 11):
    print(num * i)


# print the sum of all the numbers from 1 to n

n = int(input('enter the end? '))
total = 0
for i in range(1, n+1):
    total += i

print(total)

# print the factorial of n

n = int(input('enter the number? '))

product = 1
for i in range(1, n+1):
    product *= i

print(product)

