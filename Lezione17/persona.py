
# Giammarco Prudenzi
# Esercizi classi
'''
CLASSE: Persona

Creare un file chiamato "persona.py". In tale file, definire una classe chiamata Persona. 
Tale classe deve avere due attributi privati di tipo String, uno per il nome ed uno per il cognome, ed un attributo privato di tipo int per l'età.
- La classe Persona deve avere i seguenti metodi:

init(first_name, last_name). Tale metodo, deve verificare che first_name, last_name siano stringhe;
in caso negativo, impostare a None l'attributo che non risulta essere una stringa, stampando un messaggio di errore, ad esempio, "Il nome inserito non è una stringa!". 
Se first_name e last_name sono due stringhe, assegnare 0 all'attributo relativo all'età di una persona; 
se first_name e last_name non sono due stringhe, allora assegnare None all'età.

setName(first_name): consente di impostare il nome di una persona, modificando il valore del relativo attributo.
Il valore viene modificato se e solo se viene passata al metodo una stringa.
In caso contrario, stampare un messaggio di errore, ad esempio "Il nome inserito non è una stringa!".

setLastName(last_name): consente di impostare il cognome di una persona, modificando il valore del relativo attributo.
Il valore viene modificato se e solo se viene passata al metodo una stringa.
In caso contrario, stampare un messaggio di errore, ad esempio "Il cognome inserito non è una stringa!".

setAge(age): consente di impostare l'età di una persona, modificando il valore del relativo attributo. 
Il valore viene modificato se e solo se viene passato al metodo un numero intero.
In caso contrario, stampare un messaggio di errore, ad esempio "L'età deve essere un numero intero!".

getName(): consente di ritornare il nome di una persona.

getLastname(): consente di ritornare il cognome di una persona.

getAge(): consente di ritornare l'età di una persona.

greet(): stampa il seguente saluto "Ciao, sono nome cognome! Ho età anni!"
'''
# Svolgimento:

class Persona:
    def __init__(self):
        self.__nome = None
        self.__cognome = None
        self.__età = None
    
    def init(self, first_name: str, last_name: str):
        if type(first_name) != str:
            first_name = None
            return f"Il nome inserito non è una stringa!"
        elif type(last_name) != str:
            last_name = None
            return "Il cognome inserito non è una stringa!"
        elif type(first_name) and type(last_name) == str:
            self.__età = 0
        elif type(first_name) and type(last_name) != str:
            self.__età = None

    
    def setName(self, first_name):
        if type(first_name) == str:
            self.__nome = first_name
        else:
            return "Il nome inserito non è una stringa"
    
    def setLastName(self, last_name):
        if type(last_name) == str:
            self.__cognome = last_name
        else:
            return "Il cognome inserito non è una stringa"
        
    def setAge(self, age):
        if type(age) == int:
            self.__età = age
        else:
            return "L'età deve essere un numero intero"
    
    def getName(self):
        return f" Nome = {self.__nome}"
    
    def getLastname(self):
        return f"Cognome = {self.__cognome}"
    
    def getAge(self):
        return f"Età = {self.__età}"
    
    def greet(self):
        return f"Ciao, sono {self.__nome} {self.__cognome}! Ho {self.__età} anni!"












