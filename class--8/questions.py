# count the number of even & odd digits in the number???
'''
number = eval(input('enter the number? '))

even = 0
odd = 0

# run the loop until number becomes 0
while number > 0:
    digit = number % 10 # find the last digit

    if digit % 2 == 0: #  check if the digit is even
        even += 1 # if yes increment even
    else:
        odd += 1 # otherwise increment odd

    number = number // 10 # remove the last digit

# print the answer
print("there are", even, "even numbers in the given number")
print("there are", odd, "odd numbers in the given number")
'''

# check if a three digit number is a armstrong number or not??
'''
number = eval(input('enter the number? '))
original = number
total = 0

if number > 99 and number < 1000:
    while number > 0:
        digit = number % 10
        total = total + (digit ** 3)
        number //= 10
else:
    print("not a three digit number!!!")

if original == total:
    print("Armstrong number")
else:
    print("Not a Armstrong number")

'''


# print if a number is prime or not??
number = eval(input('enter the number? '))
i = 2
flag = 0

if number < 2:
    print("not prime")
else:
    while i < number:
        if number % i == 0:
            flag = 1
            break
        i += 1

    if flag == 0:
        print("number is prime")
    else:
        print("number is not prime")





