
# Giammarco Prudenzi

# Esercizi sulle classi 

# Biblioteca:
'''
Si desidera sviluppare un sistema per la gestione di una biblioteca in Python. 
Il sistema deve permettere di gestire un inventario di libri e le operazioni di prestito e restituzione degli stessi.
Gli utenti del sistema devono essere in grado di aggiungere libri al catalogo, prestarli, restituirli e visualizzare quali libri sono disponibili in un dato momento.
 
Classi:
- Libro: Rappresenta un libro con titolo, autore, stato del prestito. Il libro deve essere inizialmente disponibile (non prestato).

- Biblioteca: Gestice tutte le operazioni legate alla gestione di una biblioteca.

    Metodi:
    - aggiungi_libro(libro): Aggiunge un nuovo libro al catalogo della biblioteca. Restituisce un messaggio di conferma.

    - presta_libro(titolo): Cerca un libro per titolo e, se disponibile e non già prestato, lo segna come disponibile. Restituisce un messaggio di stato.

    - restituisci_libro(titolo): Cerca un libro per titolo e, se trovato e prestato, lo segna come disponibile. Restituisce un messaggio di stato.

    - mostra_libri_disponibili(): Restituisce una lista dei titoli dei libri attualmente disponibili.
    Se non ci sono libri disponibili, restituisce un messaggio di errore.

Test Cases:
- Un amministratore della biblioteca aggiunge alcuni libri all'inventario.
- Un utente prende in prestito un libro, che viene quindi marcato come non disponibile.
- L'utente restituisce il libro, che viene marcato di nuovo come disponibile.
- In qualsiasi momento, un utente può visualizzare quali libri sono disponibili per il prestito.

'''
# Svolgimento ES. Biblioteca:

class Libro:
    def __init__(self, titolo: str, autore: str, stato_del_prestito: str = "non prestato"):
        self.titolo = titolo
        self.autore = autore
        self.stato_del_prestito = stato_del_prestito

class Biblioteca:
    def __init__(self):
        self.lista_libri: list[Libro] = []
        self.libri_prestati: list[Libro] = []

    def aggiungi_libro(self,libro: Libro):
        self.lista_libri.append(libro)
        return f" il libro {libro.titolo} di {libro.autore} è stato aggiunto al catalogo"
    
    def presta_libro(self, titolo: str):
        for libro in self.lista_libri:
            if titolo.lower() == libro.titolo.lower():
                self.lista_libri.remove(libro)
                self.libri_prestati.append(libro)
                libro.stato_del_prestito = "prestato"
                return f"Il libro {libro.titolo} è disponibile per il prestito"
            else:
                
             for lib in self.libri_prestati:
                if titolo.lower() == lib.titolo.lower():
                    return f"il libro {titolo} è stato già prestato"    
                else:
                    return f"Il libro {titolo} non è persente in catalogo"
            
    def restituisci_libro(self, titolo):
        for libro in self.lista_libri:
            if libro in self.libri_prestati and libro.stato_del_prestito == "prestato":
                self.libri_prestati.remove(libro)
                self.lista_libri.append(libro)
                libro.stato_del_prestito = "non prestato"
                return f"libro disponibile per il prestito"


    def  mostra_libri_disponibili(self):
            if self.lista_libri == []:
                return f"Nessun libro disponibile"
            else:
                for libro in self.lista_libri:
                    return f"Libri disponibili:\nTitolo: {libro.titolo}\nAutore: {libro.autore}\nStato del prestito: {libro.stato_del_prestito}"


    
b = Biblioteca()
libro1 = Libro("catorcio","lupo lucio")
libro2 = Libro("la ladra di cani","alessia stuppi")
libro3 = Libro("il drago di sassi","leonardo verte")

print(b.aggiungi_libro(libro1))
print(b.aggiungi_libro(libro2))
print(b.aggiungi_libro(libro3))

print(b.lista_libri)
print(b.libri_prestati)

print(b.presta_libro("catorcio"))
print(b.presta_libro("catorcio"))
print(b.presta_libro("laico"))

print(b.mostra_libri_disponibili())







