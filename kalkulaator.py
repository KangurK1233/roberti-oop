import math

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if a == 0 or b == 0:
            return 'Nulliga ei saa jagada'
        else:
            return a / b

    def square_root(self, a):
        if a < 0:
            return 'Ruutjuurt ei saa arvutada negatiivsest arvust'
        else:
            return math.sqrt(a)
    
    def power(self, a, b):
        return math.pow(a, b)

    def sin(self, a):
        return math.sin(a)

    def cos(self, a):
        return math.cos(a)

    def tan(self, a):
        return math.tan(a)

print('----- Kngur Kalkulaator v69.420 -----')
print('Võimalikud tehted: +, -, *, /, sqrt, ^, sin, cos, tan')
print('Näidised: 5 + 5, sqrt 49, sin 20')
print('5 ^ 2, 3.3 * 3.3, 20 / 10')
print('Väljumiseks vajuta Ctrl + C')
print('-------------------------------------')

while True:
    user_input = input('Sisesta tehe: ')
    user_input = user_input.split()

    if len(user_input) == 3:
        a = float(user_input[0])
        b = float(user_input[2])
        operation = user_input[1]

        calc = Calculator()

        if operation == '+':
            print('Vastus:', calc.add(a, b))
        elif operation == '-':
            print('Vastus:', calc.subtract(a, b))
        elif operation == '*':
            print('Vastus:', calc.multiply(a, b))
        elif operation == '/':
            print('Vastus:', calc.divide(a, b))
        elif operation == 'sqrt':
            print('Vastus:', calc.square_root(b))
        elif operation == '^':
            print('Vastus:', calc.power(a, b))
        else:
            print('----------- VALE SISEND! ------------')
            print('Võimalikud tehted: +, -, *, /, sqrt, ^, sin, cos, tan')
            print('Näidised: 5 + 5, sqrt 49, sin 20')
            print('5 ^ 2, 3.3 * 3.3, 20 / 10')
            print('-------------------------------------')
    elif len(user_input) == 2 and user_input[0] == 'sqrt':
        b = float(user_input[1])
        calc = Calculator()
        print('Vastus:', calc.square_root(b))
    elif len(user_input) == 2 and user_input[0] == 'sin':
        b = float(user_input[1])
        calc = Calculator()
        print('Vastus:', calc.sin(b))
    elif len(user_input) == 2 and user_input[0] == 'cos':
        b = float(user_input[1])
        calc = Calculator()
        print('Vastus:', calc.cos(b))
    elif len(user_input) == 2 and user_input[0] == 'tan':
        b = float(user_input[1])
        calc = Calculator()
        print('Vastus:', calc.tan(b))
    else:
        print('----------- VALE SISEND! ------------')
        print('Võimalikud tehted: +, -, *, /, sqrt, ^, sin, cos, tan')
        print('Näidised: 5 + 5, sqrt 49, sin 20')
        print('5 ^ 2, 3.3 * 3.3, 20 / 10')
        print('-------------------------------------')
