def Sqrt():
    num = float(input('Please enter a number > '))
    R = num ** (1/2)

    print('The result is ' + str(R))
    return

def Square():
    num = float(input('Please enter a number > '))
    R = num ** 2

    print('The result is ' + str(R))
    return

def Cube():
    num = float(input('Please enter a number > '))
    R = num ** 3

    print('The result is ' + str(R))
    return

def Power():
    num = float(input('Please enter a number > '))
    pwr = float(input('Please enter the power > '))

    R = num ** pwr

    print('The result is ' + str(R))
    return

def other():
    x = float(input('Enter x > '))
    op = input('Enter the operator > ')
    y = float(input('Enter y > '))

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
    print('\33[33mBASIC CALCULATOR')
    print('----------------')
    print('\33[0m')

    while True:
        print()
        print('Do u want to: ')
        print('1.square root a number')
        print('2.square a number')
        print('3.cube a number')
        print('4.do any other power')
        print('5.do the other types of calculations')
        print('6. exit')

        a = input('> ')

        if(a == str(1)):
            Sqrt()
            continue
        elif(a == str(2)):
            Square()
            continue
        elif(a == str(3)):
            Cube()
            continue
        elif(a == str(4)):
            Power()
            continue
        elif(a == str(5)):
            other()
            continue
        elif(a == str(6)):
            break
        else:
            print('ERROR 404')
            continue
    return

Main()

input('Press enter to exit...')
exit()
