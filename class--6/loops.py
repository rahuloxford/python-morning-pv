# while loops??

# syntax of while loop
'''
variable
while condition:
    code1
    code2
    code3

    increment / decrement
'''

# print "Hello World" 10 times.
'''
count = 1
while count <= 10:
    print(count)
    count = count + 1
'''

# print 1 to n
'''
i = 1
n = eval(input('enter the end? ')) # 5

while i <= n:
    print(i)
    i = i + 1
'''

# print from n to 1.
'''
i = 1
n = eval(input('enter the end? ')) # 5

while i <= n:
    print(i)
    i = i - 1
'''

# print the table of n.
'''
n = eval(input('enter the number you want the table of? ')) # 5

i = 1
while i <= 10:
    print(n * i)
    i += 1
'''

# print the sum of all the numbers from 1 to n.
i = 1
n = eval(input('enter the end? '))

total = 0
while i <= n:
    total = total + i
    i = i + 1

print(total)

