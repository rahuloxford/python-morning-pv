# print all the even numbers from 1 to 100

i = 1
while i <= 100:
    if i % 2 == 0:
        print(i)
    i += 1


# count the number of digits in a number?

number = eval(input('enter a number here? '))

count = 0
while number > 0:
    number = number // 10
    count = count + 1

print("there are", count, "digits in this number")


# print the sum of all the digits in a number?

number = eval(input('enter a number here? '))
total = 0
while number > 0:
    last_digit = number % 10
    total = total + last_digit
    number = number // 10

print("the sum of all the digits in the number is:",total)


# print the number in reverse order given by the user?
# example: if user gave: 1234 -> 4321

number = eval(input('enter a number here? '))

reverse = 0
while number > 0:
    last_digit = number % 10
    reverse = reverse * 10 + last_digit
    number = number // 10

print(reverse)



 
