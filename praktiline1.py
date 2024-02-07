import random

'''
Testimiseks vajutasin nimetis sõrmega enda hiirel vasakut nuppu, et kood käivitada.
Koodi funktsionaalsuse testimisel vaatasin, et mängijad ründavad üksteist ja kui mängija elud on otsas, siis mäng lõppeb.
'''

class Warrior:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health

    def attack(self, enemy):
        print(f"{self.name} ründas {enemy.name}!")
        enemy.health -= 20
        if enemy.health <= 0:
            print(f"{enemy.name} sai vastu kotte. {self.name} võitis. Sõda läbi.")
            return True
        else:
            print(f"{enemy.name} on {enemy.health} elu jäänud.")
            return False

warrior1 = Warrior("Robertallan")
warrior2 = Warrior("Ott Kukk")

while True:
    attacker = random.choice([warrior1, warrior2])
    defender = warrior2 if attacker == warrior1 else warrior1
    if attacker.attack(defender):
        break