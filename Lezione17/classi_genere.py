
# Giammarco Prudenzi

# CLASSI GENERE
'''
Si creino tre classi chiamate Azione, Commedia e Drama, tutte derivanti dalla classe Film. 
Ognuna di queste classi ha un attributo privato di tipo string chiamato genere, 
che equivale al genere di film (genere="Azione", nella classe Azione) ed un attributo privato di tipo float chiamato penale. 
I film di azione hanno una penalità di 3 euro al giorno, le commedie hanno una penale di 2.50 euro al giorno, i film drammatici hanno una penale di 2 euro al giorno.

- Per ognuna di queste classi si implementi un metodo chiamato:

    getGenere(), che ritorna il genere di film
    getPenale(), che ritorna il valore della penale
    calcolaPenaleRitardo(), che prende in ingresso il numero dei giorni di ritardo per un film e restituisce la penale da pagare per quel film.

Le tre classi Azione, Commedia e Drama devono essere contenute nel file "movie_genre.py".
'''
# classi genere
# Svolgimento:

from film import Film

class Azione(Film):
    def __init__(self, id: str, title: str, __genere: str = "Azione"):
        super().__init__(id, title)


class Commedia(Film):
    def __init__(self, id: str, title: str, __genere: str = "Commedia"):
        super().__init__(id, title)


class Drama(Film):
    def __init__(self, id: str, title: str, __genere: str = "Drama"):
        super().__init__(id, title)