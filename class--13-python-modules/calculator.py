
def add(*nums):
    total = 0
    for i in nums:
        total += i
    return total

def product(*nums):
    product = 1
    for i in nums:
        product *= i
    return product


if __name__ == "__main__":
    print(add(45, 89, 68))
    print(product(98, 23))

