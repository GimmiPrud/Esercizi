
# Giammarco Prudenzi
# Esercizi sulle classi
'''
Creare un file chiamato "paziente.py".
In tale file, creare una classe chiamata Paziente. Si derivi Paziente dalla classe Persona.

Un paziente ha un nome, un cognome, un età, definiti dalla classe Persona ed un codice identificativo (si usi il tipo String).
- Definire i seguenti metodi:

costruttore della classe paziente, il quale richiede in input il codice identificativo, il quale deve essere un attributo privato.
setIdCode(idCode): consente di impostare il codice identificativo del paziente.

getidCode(): consente di ritornare il codice identificativo del paziente.

patientInfo(): stampa in output le informazioni del paziente in questo modo:

"Paziente: {nome} {cognome}
    ID: {codice identificativo}"
'''
# Svolgimento:

from persona import Persona

class Paziente(Persona):
    def __init__(self):
        super().__init__()
        self.__id = None

    def setIdCode(self,idCode):
        self.__id = idCode

    def getidCode(self):
        return f"Codice identificativo: {self.__id}"
    
    def patientInfo(self):
        return f"Paziente: {self.__nome} {self.__cognome}\nID: {self.__id}"
