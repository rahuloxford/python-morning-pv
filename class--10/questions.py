
random_number = 45



while True:
    n = int(input('guess the number? '))
    if n == random_number:
        break
    else:
        print('try again')

print('congrats you guessed it')      
