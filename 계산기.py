def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a, b):
    return a / b

while True:
    num1 = int(input('Frist Number :'))
    num2 = int(input('Second Number :'))
    code = input('selet : ')
    if code == '+':
        result = add(num1, num2)
        print(f'결과 : {result}')
    elif code == '-':
        result = subtract(num1, num2)
        print(f'결과 : {result}')
    elif code == '*':
        result = multiply(num1, num2)
        print(f'결과 : {result}')
    elif code == '/':
        result = divide(num1, num2)
        print(f'결과 : {result}')
    replay = input('계속 하시겠습니까 y/n :')
    if replay == 'n':
        break