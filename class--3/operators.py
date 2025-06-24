# operators - symbols that performs an operation.

# Arithemetic operators [ +, -, *, /, //, **, % ]
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3) # integer division
print(5 ** 7) # exponent
print(5 % 3) # modulas


# Comparison operators [ >, >=, <, <=, ==, != ]
print(5 > 5) # greater than
print(5 >= 5) # greater than or equal to
print(3 < 3) # less than
print(4 <= 4) # less than or equal to
print(8 == 8) # equal to
print(5 != 2) # not equal


# Logical operators [ and, or, not ]
# and - True only if all operands are True
print(True  and True)
print(True  and False)
print(False  and True)
print(False  and False)
# or - False only if all operands are False
print(True  or True and False)
print(True  or False)
print(False  or True)
print(False  or False or True)
# not - Invert the value
print(not True)
print(not False)

# REAL LIFE EXAMPLE:
age = 25
gender = "female"
print(not age >= 18 or gender == "male")


# Identity operators [ is, is not ]

food = "burger"
print(food is "pizza")
print(food is not "pizza")

# Membership operators [ in, not in ]

show = "ramayana"

print("ram" in show)
print("ram" not in show)



# precedence in operators

'''

()
**
/, *, %, //
+, -
>, >=, <, <=, ==, !=, in, not in, is, is not
not
and
or

'''






