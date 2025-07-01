
# collections: list, tuple, set, dict, range

# list are hetrogenous
# list is created using square brackets [], each item is seperated with the help of comma ,
# list: ordered, support indexing, duplicates supported, mutable (changeable)

data = [156, "tim", 96.37, True, 894, 156]

print(data)
print(data[3])
print(type(data))

data.append(894)
data.pop(3)

data[0] = 101
print(data)

temp = data.copy()

temp[0] = 1000

print(temp)
print(data)


# tuple is exactly same as list, only difference is it is imutable
# tuple is created using square brackets (), each item is seperated with the help of comma ,
# tuple: ordered, support indexing, duplicates supported, imutable (unchangeable)

data2 = (156, "tim", 96.37, True, 894, 156)

print(data2)
print(data2[1])
print(type(data2))

data2.pop(2)


