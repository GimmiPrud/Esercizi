
# Giammarco Prudenzi
# Esercizi sulle classi

'''
Creare un file chiamato "dottore.py".
In tale file, definire una classe chiamata Dottore. Si derivi Dottore dalla classe Persona.

Un dottore ha un nome, un cognome, un età, definiti dalla classe Persona,
una specializzazione descritta tramite una stringa (ad esempio, Pediatra, Ostetrico, Medico Generale),ed una parcella per le visite in studio (si usi il tipo float).
Gli attributi della classe dottore devono essere anch'essi privati.

- Definire i seguenti metodi:

costruttore della classe Dottore, il quale richiede in input la specializzazione (specialization) di un dottore e la sua parcella (parcel).
Tale metodo deve controllare che specialization sia una stringa e che parcel sia un float,
altrimenti assegna None all'attributo che non verifica la condizione richiesta, mostrando un messaggio di errore, ad esempio, "La parcella inserita non è un float!".

setSpecialization(specialization): consente di impostare la specializzazione di un dottore, modificando il valore del relativo attributo.
Il valore viene modificato se e solo se viene passata al metodo una stringa.
In caso contrario, stamapre un messaggio di errore, ad esempio "La specializzazione inserita non è una stringa!".

setParcel(parcel): consente di impostare la parcella di un dottore, modificando il valore del relativo attributo.
Il valore viene modificato se e solo se viene passato al metodo un float.
In caso contrario, stamapre un messaggio di errore, ad esempio "La parcella inserita non è un float!".

getSpecialization(): consente di ritornare la specializzazione del dottore.

getParcel(): consente di ritornare la parcella del dottore.

isAValidDoctor(): stabilisce se un dottore è un dottore valido;
un dottore è valido se e solo se ha più di 30 anni, in quanto ha avuto il tempo necessario di compiere i suoi studi in medicina.
Stampare "Doctor nome e cognome is valid!", se il dottore risulta valido. In caso contrario, stampare "Doctor nome e cognome is not valid!".

doctorGreet():tale metodo richiama la funzione greet() della classe Persona.
Poi, stampa il seguente saluto "Sono un medico {specializzazione}"
'''
# Svolgimento:

from persona import Persona

class Dottore(Persona):
    
    def __init__(self, __nome: str, __cognome: str, __età: int, __specializzazione: str, __parcella: float):
        super().__init__(__nome, __cognome, __età)
        self.__specializzazione = __specializzazione
        self.__parcella = __parcella
    
    def init(self, specialization: str, parcel: float):
        if type(specialization) != str:
            self.__specializzazione = None
            return "La specializzazione inserita non è una stringa!"
        elif type(parcel) != float:
            self.__parcella = None
            return "La parcella inserita non è un float!"
    
    def setSpecialization(self, specialization: str):
        if type(specialization) == str:
            self.__specializzazione = specialization
        else:
            return "La specializzazione inserita non è una stringa!"
        
    def setParcel(self, parcel):
        if type(parcel) == str:
            self.__parcella = parcel
        else:
            return "La parcella inserita non è un float!"
        
    def getSpecialization(self):
        return f"Specializzazione: {self.__specializzazione}"
    
    def getParcel(self):
        return f"Parcella: {self.__parcella}"
    
    def isAValidDoctor(self):
        if self.__età > 30:
            return "Doctor nome e cognome is valid!"
        else:
            return "Doctor nome e cognome is not valid!"
        
    def doctorGreet(self):
        return self.greet(),f"\nSono un medico {self.__specializzazione}"
    




