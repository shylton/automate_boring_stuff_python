
def collatz(number):
    return number // 2 if number % 2 == 0 else (3 * number) + 1


x = input('Enter an integer greater than one => ')

try:
    x = int(x)

    while x > 1:
        x = collatz(x)
        print(x)
except ValueError as err:
    print('ERROR:', err)
    

      
