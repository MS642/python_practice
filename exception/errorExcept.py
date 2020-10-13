
try:
    for i in ['a','b','c']:
        print(i**2)
except Exception as e:
    print(f'Error {e}')

try:
    x = 5
    y = 0

    z = x / y
except ZeroDivisionError as z:
    print(f'Error {z}')
finally:
    print('All Done!')


def ask():
    while True:
        try:
            square = int(input('Provide a number to square:'))**2
        except:
            print("An Error has occured, Please try again")
        else:
            print(f'Thank you! The square is {square}')
            break


ask()

