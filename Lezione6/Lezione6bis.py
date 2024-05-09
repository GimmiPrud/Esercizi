# Giammarco Prudenzi                         09/05/2024
# Esercizi sulle classi e sull'ereditarietà

from typing import Tuple


class Person:                 # questa è una superclasse (classe padre)
    def __init__(self,
                nome: str,
                cognome: str,
                genere: str,
                data_di_nascita: str):
        
        self.nome = nome
        self.cognome = cognome
        self.genere = genere
        self.data_di_nascita = data_di_nascita

    def calcola_età(self)-> int:
        return 5    
    
class Dipendente(Person):  # questa è una sottoclasse cioè la classe che erediterà le caratteristiche della classe padre(superclasse)
    def __init__(self, nome: str, cognome: str, genere: str, data_di_nascita: str):
         super().__init__(nome, cognome, genere, data_di_nascita)  # le caratteristiche dell'init vengono prese automaticamente  

    def calcola_stipendio(self):
        return 1500           # questa funzione è all'interno della sottoclasse dipendente e verrà visto solo dalla sottoclasse 
                              # quindi non verrà visto dalla classe padre(superclasse)(Person)

persona1 = Person(nome="Luca",
                  cognome="Caprasecca",
                  genere= "M",
                  data_di_nascita="09/05/2024")
       

dipendente1 = Dipendente(nome="Luca",
                  cognome="Caprasecca",
                  genere= "M",
                  data_di_nascita="09/05/2024")

print(dipendente1.calcola_età())
print(dipendente1.calcola_stipendio())
print(persona1.calcola_età())