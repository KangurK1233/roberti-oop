import random

class Lumi:
    def __init__(self, helveste_arv):
        self.helveste_arv = helveste_arv
    
    def __add__(self, n):
        self.helveste_arv += n
        return self
    
    def __sub__(self, n):
        self.helveste_arv -= n
        return self
    
    def __mul__(self, n):
        self.helveste_arv *= n
        return self
    
    def __truediv__(self, n):
        self.helveste_arv = int(self.helveste_arv / n)
        return self
    
    def makeSnow(self):
        return '\n'.join(['*' * self.helveste_arv for _ in range(self.helveste_arv)])

# Testimine
lumi = Lumi(random.randint(5, 15))  # Loome juhusliku lumehelveste arvuga objekti

print("Algseis:")
print(lumi.makeSnow())

lumi += 3  # Lisame 3 lumehelvest
print("\nPärast liitmist:")
print(lumi.makeSnow())

lumi -= 2  # Vähendame 2 lumehelvest
print("\nPärast lahutamist:")
print(lumi.makeSnow())

lumi *= 2  # Korrutame lumehelveste arvu kahekordseks
print("\nPärast korrutamist:")
print(lumi.makeSnow())

lumi /= 3  # Jagame lumehelveste arvu 3-ga ja ümardame täisarvuni
print("\nPärast jagamist:")
print(lumi.makeSnow())
