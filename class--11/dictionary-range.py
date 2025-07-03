
# dictionary

student = {'name':'tom olsen', 'id':23592, 'age':25}

print(student)
print(student['age'])

print(student.keys())
print(student.values())
print(student.items())

emps = {1596:'tim', 9875:'jon', 9725:'lewis', 1472:'max'}
print(emps[9725])

phones = {'max':'samsung s25', 'lewis':'iphone 15', 'kimi':'motorola edge 60'}
print(phones['max'])


# range

# first way
i = range(10)
print(list(i))


# second way
j = range(25, 50)
print(list(j))


# third way
k = range(10, 50, 3)
print(list(k))


k2 = range(50, 9, -1)


