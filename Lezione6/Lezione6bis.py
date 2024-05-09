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
    def __init__(self, nome: str, cognome: str, genere: str, data_di_nascita: str, ore_lavorate: int):
         
         super().__init__(nome, cognome, genere, data_di_nascita)  # le caratteristiche dell'init vengono prese automaticamente  
         
         self.ore_lavorate = ore_lavorate # questo è un attributo specifico della sottoclasse che la superclasse non può vedere 

    def calcola_stipendio(self):
        return 1500            # questa funzione è all'interno della sottoclasse dipendente e verrà visto solo dalla sottoclasse 
                               # quindi non verrà visto dalla classe padre(superclasse)(Person)

class Professore(Dipendente):   # sottoclasse di una sottoclasse 

    def __init__(self, nome: str, cognome: str, genere: str, data_di_nascita: str, ore_lavorate: int,
                 materia_insegnata: str, ore_di_lezione: int):

        super().__init__(nome, cognome, genere, data_di_nascita, ore_lavorate)

        self.materia_insegnata = materia_insegnata
        self.ore_di_lezione = ore_di_lezione
    

    def __eq__(self, value: object) -> bool:  # metodo che rappresenta l'uguaglianza (si utilizza per confrontare gli oggetti)
        return super().__eq__(value)
    
    def __repr__(self) -> str:  # si utilizza per ispezionare gli oggetti ed avere informazioni (debug)
        return super().__repr__()


persona1 = Person(nome="Luca",
                  cognome="Caprasecca",
                  genere= "M",
                  data_di_nascita="09/05/2024")       

dipendente1 = Dipendente(nome="Luca",
                  cognome="Caprasecca",
                  genere= "M",
                  data_di_nascita="09/05/2024",
                  ore_lavorate= 500)

professore1 = Professore(nome="Luca",
                  cognome="Caprasecca",
                  genere= "M",
                  data_di_nascita="09/05/2024",
                  ore_lavorate=500,
                  materia_insegnata="Storia",
                  ore_di_lezione=40)


print(dipendente1.calcola_età())
print(dipendente1.calcola_stipendio())
print(persona1.calcola_età())
print(dipendente1.ore_lavorate)
print(professore1.materia_insegnata)
print(professore1.ore_di_lezione)