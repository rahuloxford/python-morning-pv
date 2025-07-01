# list is used to store multiple elements inside a single variable.
# list is hetrogenous in nature.
# list is ordered, allows indexing, allows duplicates, and is mutable (changeable).
data1 = [18, "tom", True, 986.23, "tom", 18]
print(data1)
print(type(data1))
print(data1[3])

data1.append(46)
print(data1)
print(data1.pop())
data1.remove(18)
print(data1.count("tom"))
print(data1.index(True))
data1.insert(2, 465)
print(data1)
data1.extend([56, 89, 75])
print(data1)
data2 = data1.copy()
#print(id(data1))
#print(id(data2))
data2[0] = 301
print(data1)
print(data2)

#data1.clear()
data2 = [165, 79, 489, 216, 19]
data2.sort()
data2.reverse()
print(data2)


print("--------------------------------")

# tuple
# tuple is used to store multiple elements inside a single variable.
# tuple is hetrogenous in nature.
# tuple is ordered, allows indexing, allows duplicates, and is imutable (unchangeable).

data3 = (16, 98, 46, 16, 3.5, "chris")
print(data3)
print(data3[2])


print(data3.index("chris"))
print(data3.count(16))


print("--------------------------------")


# set
# set is used to store multiple elements inside a single variable.
# set is hetrogenous in nature.
# set is unordered, does'nt allows indexing, does'nt allows duplicates, and is mutable (changeable).

data4 = {89, 56, 3.25, "chris", 79, 56, 13, 56}

print(data4)
#print(data4[0])

data4.add(234)
print(data4)

data4.remove(3.25)
print(data4)

