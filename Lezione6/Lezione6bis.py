
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

#////////////////////////////////////////////////////////////////////////////////////////#

# Come funzionano le classi
# Spiegazione ed esempi di ripasso:


from abc import ABC, abstractmethod  # abstractmethod è un decorator (i decorator usano il cls=@) 
                                     # abstractmethod deve essere importato per essere utilizzato 
class AbcAnimal(ABC):   # facciamo ereditare la funzione ABC alla classe

    @abstractmethod # si utilizza per creare una classe astratta 
    def verso(self):
        pass
    
    @abstractmethod
    def movimento(self):
        pass


class cane(AbcAnimal):  # Sottoclasse di AbcAnimal 

    def __init__(self, nome: str) -> None:
        super().__init__()

        self.nome = nome
        self.velocità: float = 10 # m/s
    
    def verso(self):
        print("Bau")
    
    def movimento(self, t: int):
        print(self.velocità*t)


cane1 = cane(nome= "Ulisse")
print(cane1.nome)
cane1.verso()
cane1.movimento(t=10)


class gatto(AbcAnimal):

    def __init__(self, nome: str) -> None:
        super().__init__()

        self.nome = nome
        self.velocità: float = 15.0 # m/s
    
    def verso(self):
        print("Miao")

    def movimento(self, t: float):
        print(self.velocità*t)

gatto1 = gatto(nome= "kitty")
print(gatto1.nome)
gatto1.verso()
gatto1.movimento(15)


#/////////////////////////////////////////////////////////////#

class contobancario():

    total_accounts = 0

    def __init__(self,iban, saldo, nome):
        self.iban = iban
        self.nome = nome
        self.saldo = saldo

        contobancario.total_accounts += 1 # questo permette di chiamare la variabile di classe globale 
                                          # questa variabile aumenterà ogni volta che si chiamerà la classe 
    
    def deposito(self,importo):
        self.saldo += importo
        print(f"{importo}£ depositati. il nuovo saldo è {self.saldo}£")

    def prelievo(self, importo):
        self.saldo -= importo
        print(f"{importo}£ prelevati. il nuovo saldo è {self.saldo}£")
    
    @classmethod # metodo che si chiama e rigurda tutta la classe e non le singole istanza (come se fosse un metodo globale della Classe )

    def get_total_accounts(cls):
        print(f"Account totali creati: {cls.total_accounts}")
    
    @staticmethod # 

    def valida_account(iban):
        if isinstance(iban, int) and len(str(iban))==10:
            print("iban valido")
            return True
        else:
            print("iban non valido")
            return False

account1 = contobancario(1345566789,0,"Luca")
account2 = contobancario(4789654306,100,"Loris")
account1.deposito(300)
account2.deposito(100)
account1.prelievo(250)
account2.prelievo(75)
contobancario.get_total_accounts()


