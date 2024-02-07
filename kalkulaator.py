import math

# Kalkulaatori klass
class Calculator:
    
    # Liitmise meetod
    def add(self, a, b):
        return a + b

    # Lahutamise meetod
    def subtract(self, a, b):
        return a - b

    # Korrutamise meetod
    def multiply(self, a, b):
        return a * b

    # Jagamise meetod
    def divide(self, a, b):
        if a == 0 or b == 0:
            return 'Nulliga ei saa jagada'
        else:
            return a / b

    # Ruutjuure arvutamise meetod
    def square_root(self, a):
        if a < 0:
            return 'Ruutjuurt ei saa arvutada negatiivsest arvust'
        else:
            return math.sqrt(a)
    
    # Astme arvutamise meetod
    def power(self, a, b):
        return math.pow(a, b)

    # Sinuse arvutamise meetod
    def sin(self, a):
        return math.sin(a)

    # Kosinuse arvutamise meetod
    def cos(self, a):
        return math.cos(a)

    # Tangensi arvutamise meetod
    def tan(self, a):
        return math.tan(a)

# Abiinfo kasutajale
print('----- Kngur Kalkulaator v69.420 -----')
print('Võimalikud tehted: +, -, *, /, sqrt, ^, sin, cos, tan')
print('Näidised: 5 + 5, sqrt 49, sin 20')
print('5 ^ 2, 3.3 * 3.3, 20 / 10')
print('Väljumiseks vajuta Ctrl + C')
print('-------------------------------------')

# Kalkulaatori kasutamine
while True:
    # Kasutaja sisend ja selle töötlemine
    user_input = input('Sisesta tehe: ')
    user_input = user_input.split()

    # Kui kasutaja sisend on 3 sõna pikk, siis teostatakse liitmise, lahutamise, korrutamise, jagamise või astme arvutamine
    if len(user_input) == 3:
        # Tehte numbrid ja operaator
        a = float(user_input[0])
        b = float(user_input[2])
        operation = user_input[1]

        # Kalkulaatori objekti loomine
        calc = Calculator()

        # Kui operaator on +, -, *, / või ^, siis teostatakse vastav arvutus
        if operation == '+':
            print('Vastus:', calc.add(a, b))
        elif operation == '-':
            print('Vastus:', calc.subtract(a, b))
        elif operation == '*':
            print('Vastus:', calc.multiply(a, b))
        elif operation == '/':
            print('Vastus:', calc.divide(a, b))
        elif operation == '^':
            print('Vastus:', calc.power(a, b))
        else:
            # Kui operaator on midagi muud, siis väljastatakse veateade
            print('----------- VALE SISEND! ------------')
            print('Võimalikud tehted: +, -, *, /, sqrt, ^, sin, cos, tan')
            print('Näidised: 5 + 5, sqrt 49, sin 20')
            print('5 ^ 2, 3.3 * 3.3, 20 / 10')
            print('-------------------------------------')
    # Kui kasutaja sisend on 2 sõna pikk, siis teostatakse ruutjuure, sinuse, kosinuse või tangensi arvutamine
    elif len(user_input) == 2 and user_input[0] == 'sqrt':
        # Kui kasutaja sisend on 2 sõna pikk ja esimene sõna on 'sqrt', siis teostatakse ruutjuure arvutamine
        b = float(user_input[1])
        calc = Calculator()
        print('Vastus:', calc.square_root(b))
    elif len(user_input) == 2 and user_input[0] == 'sin':
        # Kui kasutaja sisend on 2 sõna pikk ja esimene sõna on 'sin', siis teostatakse sinuse arvutamine
        b = float(user_input[1])
        calc = Calculator()
        print('Vastus:', calc.sin(b))
    elif len(user_input) == 2 and user_input[0] == 'cos':
        # Kui kasutaja sisend on 2 sõna pikk ja esimene sõna on 'cos', siis teostatakse kosinuse arvutamine
        b = float(user_input[1])
        calc = Calculator()
        print('Vastus:', calc.cos(b))
    elif len(user_input) == 2 and user_input[0] == 'tan':
        # Kui kasutaja sisend on 2 sõna pikk ja esimene sõna on 'tan', siis teostatakse tangensi arvutamine
        b = float(user_input[1])
        calc = Calculator()
        print('Vastus:', calc.tan(b))
    else:
        # Kui kasutaja sisend on midagi muud, siis väljastatakse veateade
        print('----------- VALE SISEND! ------------')
        print('Võimalikud tehted: +, -, *, /, sqrt, ^, sin, cos, tan')
        print('Näidised: 5 + 5, sqrt 49, sin 20')
        print('5 ^ 2, 3.3 * 3.3, 20 / 10')
        print('-------------------------------------')
