'''
with open("dcu.txt", "a") as myfile:
    myfile.write("\ni am flash")
'''


with open("dcu.txt", "r") as myfile:
    #print(myfile.readline())
    #print(myfile.readline())
    #print(myfile.read(10))
    print(myfile.read())
