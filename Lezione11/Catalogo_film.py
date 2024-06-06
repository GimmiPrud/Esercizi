
# Giammarco Prudenzi 

# Esericzi sulle calssi 

# Catalogo_film:
'''
Sviluppa un sistema in Python per la gestione di un catalogo film che permetta di aggiungere, rimuovere e cercare film di un particolare regista.
Il sistema dovrebbe consentire anche di visualizzare tutti i registi e i loro film.

Classe:
- MovieCatalog: Gestisce tutte le operazioni legate al catalogo dei film.

Metodi:
- add_movie(director_name, movies): Aggiunge uno o più film a un regista specifico nel catalogo.
Se il regista non esiste, viene creato un nuovo record. Se il regista esiste, la sua lista di film viene aggiornata.

- remove_movie(director_name, movie_name): Rimuove un film specifico dall'elenco dei film di un regista.
Se tutti i film sono rimossi, il regista può essere opzionalmente rimosso dal catalogo.

- list_directors(): Elenca tutti i registi presenti nel catalogo.

- get_movies_by_director(director_name): Restituisce tutti i film di un regista specifico.

- search_movies_by_title(title): Trova tutti i film che contengono una certa parola nel titolo.
Restituisce un elenco dei registi e dei rispettivi film che contengono la parola cercata o 
un messaggio di errore se nessun film contiene la parola cercata nel titolo.

'''
# Svolgimento ES. Catalogo_film:

class Moviecatalog:
    
    def __init__(self):
        
        self.directors = {}
    
    def add_movie(self, director_name, movies):
        self.directors[director_name]= movies
        for k,v in self.directors.items():
            if director_name == k:
                v += movies
            elif movies == v:
                pass
                
                
            
            
        
    def remove_movie(self, director_name, movie_name):
        pass
    
    def list_directors(self):
        for directors in self.directors.keys():
            return directors
    
    def search_movie_by_title(self,title):
        pass
    
    def get_movies_by_director(self,director_name):
        pass
    


catalogo1 = Moviecatalog()

catalogo1.add_movie( director_name="Martin Scorsese", movies="Taxi Driver")
catalogo1.add_movie("Quentin Tarantino","Le iene")
catalogo1.add_movie("Christopher Nolan","Inception")
catalogo1.add_movie("Christopher Nolan","Il cavaliere oscuro")

print(catalogo1.directors)