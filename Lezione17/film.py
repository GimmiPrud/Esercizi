
# Giammarco Prudenzi

# CLASSE: Film
'''
In un file chiamato "film.py", si definisca la classe Film che rappresenta un film preso a nolleggio. In tale classe, definire un codice identificativo (int) ed un titolo (string). Entrambi gli attributi sono da considerarsi privati.
 
- Definire i seguenti metodi:

    init(id, title): metodo costruttore.
    setID(id): che consente di impostare il codice identificativo del film, modificando il valore del relativo attributo.
    setTitle(title): che consente di impostare il codice identificativo del film, modificando il valore del relativo attributo.
    getID(): che consente di ritornare il valore del codice identificativo di un film.
    getTitle(): che consente di ritornare il valore del titolo di un film.
    isEqual(otherFilm): che ritorna true se il codice identificativo di due film è uguale.  
'''
# Svolgimento:

class Film:

    def __init__(self, id: str, title: str):
        self.id = id
        self.title = title

    def set_ID(self, id: str):
        self.id = id
    
    def set_Title(self, title: str):
        self.title = title
        return self.title
    
    def getID(self):
        return f"id film: {self.id}"
    
    def getTitle(self):
        return f"Titolo film: {self.title}"
    
    def isEqual(self, otherFilm):
        pass






    


