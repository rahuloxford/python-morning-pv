# variable = open(filename, mode)

'''
with open("marvel.txt") as file:
    print(file.readline())
    print(file.readline())
'''

with open("marvel.txt", "a") as f:
    f.write("I am tom\n")

with open("marvel.txt") as file:
    #print(file.read())
    count = 1
    for i in file.readlines():
        if count == 3:
            print(i)
            break
        count += 1
