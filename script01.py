
def Sqrt():
    print('Please enter a number: ')

    num = float(input())
    R = num ** (1/2)

    print('The result is ' + str(R))
    return

def Square():
    print('Please enter a number: ')

    num = float(input())
    R = num ** 2

    print('The result is ' + str(R))
    return

def Cube():
    print('Please enter a number: ')

    num = float(input())
    R = num ** 3

    print('The result is ' + str(R))
    return

def Power():
    print('Please enter a number: ')

    num = float(input())

    print('Please enter the power: ')

    pwr = float(input())

    R = num ** pwr

    print('The result is ' + str(R))
    return

def other():
    x = float(input('Enter x: '))
    op = input('Enter the operator: ')
    y = float(input('Enter y: '))

    if(op == '+'):
        result = float(x + y)
        print('The result is: ' + str(result))
    elif(op == '-'):
        result = float(x - y)
        print('The result is: ' + str(result))
    elif(op == '*'):
        result = float(x * y)
        print('The result is: ' + str(result))
    elif(op == '/'):
        result = float(x / y)
        print('The result is: ' + str(result))
    elif(op == '/'):
        result = float(x / y)
        print('The result is: ' + str(result))
    else:
        print('ERROR 404')
        return

def Main():
    print('Do u want to: ')
    print('1.square root a number')
    print('2.square a number')
    print('3.cube a number')
    print('4.do any other power')
    print('5.do the other types of calculations')

    a = input()

    if(a == str(1)):
        Sqrt()
    elif(a == str(2)):
        Square()
    elif(a == str(3)):
        Cube()
    elif(a == str(4)):
        Power()
    elif(a == str(5)):
        other()
    else:
        print('ERROR 404')
        return

Main()

print('Press enter to exit...')
input()
