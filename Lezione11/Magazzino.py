
# Giammarco Prudenzi

# Esercizi sulle classi

# Cinema:
'''
Scrivi un programma in Python che gestisca un magazzino. Il programma deve permettere di aggiungere prodotti al magazzino, cercare prodotti per nome e verificare la disponibilità di un prodotto.

Definisci una classe Prodotto con i seguenti attributi:
- nome (stringa)
- quantità (intero)
 
Definisci una classe Magazzino con i seguenti metodi:
- aggiungi_prodotto(prodotto: Prodotto): aggiunge un prodotto al magazzino.
- cerca_prodotto(nome: str) -> Prodotto: cerca un prodotto per nome e lo ritorna se esiste.
- verifica_disponibilità(nome: str) -> str: verifica se un prodotto è disponibile in magazzino.
 
Test case:
Un gestore del magazzino crea un magazzino e diversi prodotti in diverse quantità. Successivamente, aggiunge i prodotti al magazzino.
Il sistema cerca un prodotto per verificare se esiste nell'inventario.
Il sistema verifica la disponibilità dei prodotti in inventario.
'''
# Svolgimento ES. Magazzino:

class Prodotto:
    def __init__(self, nome: str, quantità: int):
        self.nome = nome
        self.quantità = quantità
        
class Magazzino:
    def __init__(self):
        pass
    
    def aggiungi_prodotto(self, prodotto: Prodotto):
        pass
    
    def cerca_prodotto(self, nome: str)-> Prodotto:
        pass
    
    def verifica_disponibilità(self, nome: str)-> str:
        pass