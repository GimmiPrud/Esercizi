
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
    
    def getID(self):
        return f"id film: {self.id}"
    
    def getTitle(self):
        return f"Titolo film: {self.title}"
    
    def isEqual(self, otherFilm):
        if self.id.lower() == otherFilm.id.lower():
            return True
        else:
            return False 


film1 = Film("1234","Shutter island")
# print(film1.getID())
# print(film1.getTitle())
# film1.set_ID("5632")
# film1.set_Title("Kill Bill vol 1")
# print(film1.getID())
# print(film1.getTitle())


film2 = Film("1234","Maze Runner")
# print(film2.getID())
# print(film2.getTitle())
# film2.set_ID("4879")
# film2.set_Title("Scarface")
# print(film2.getID())
# print(film2.getTitle())

print(film1.isEqual(film2))

        






    


