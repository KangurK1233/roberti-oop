import random

'''
Testimiseks vajutasin nimetis sõrmega enda hiirel vasakut nuppu, et kood käivitada.
Koodi funktsionaalsuse testimisel vaatasin, et isikud on loodud ja nende kvalifikatsioon on ka genereeritud. Samuti kontrollisin, et kõige nõrgem lüli on kustutatud.
'''

class Person:
    def __init__(self, first_name, last_name, qualification=1):
        self.first_name = first_name
        self.last_name = last_name
        self.qualification = qualification
    
    def get_info(self):
        return f"Nimi: {self.first_name} {self.last_name}, Kvalifikatsioon: {self.qualification}"

    def delete(self):
        print(f"Hüvasti, {self.first_name} {self.last_name}!")
        del self

# Loome kolm Isiku objekti
person1 = Person("John", "Doe", qualification=random.randint(1, 20))
person2 = Person("Joe", "Average", qualification=random.randint(1, 20))
person3 = Person("Yuri", "Tarded", qualification=random.randint(1, 20))

# Vaatame töötajate teavet
print(person1.get_info())
print(person2.get_info())
print(person3.get_info())

# Vallandame nõrgima lüli, kus kvalifikatsioon on madalaim
weakest_link = min(person1, person2, person3, key=lambda x: x.qualification)
weakest_link.delete()


# Ootame, kuni kasutaja vajutab Enterit
input("Vajuta Enterit, et lõpetada...")