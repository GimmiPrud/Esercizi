
# Giammarco Prudenzi 

# Esercizi sulle classi:

# Cinema:
'''
Sistema di Prenotazione Cinema

Sviluppa un sistema in Python che gestisca le prenotazioni per un cinema.
 Il cinema ha diverse sale, ognuna con un diverso film in programmazione.
 Gli utenti possono vedere quali film sono disponibili e prenotare posti per un determinato spettacolo.
 
Classi:
- Film: Rappresenta un film con titolo e durata.
- Sala: Rappresenta una sala con numero identificativo, film attualmente in programmazione, posti totali, posti prenotati.

Metodi:
    - prenota_posti(num_posti): Prenota un certo numero di posti nella sala, se disponibili.
    Restituisce un messaggio di conferma o di errore.
    - posti_disponibili(): Restituisce il numero di posti ancora disponibili nella sala.
 
- Cinema: Gestisce le operazioni legate alla gestione delle sale.

Metodi:
    - aggiungi_sala(sala): Aggiunge una nuova sala al cinema.
    - prenota_film(titolo_film, num_posti): Trova il film desiderato e tenta di prenotare posti. Restituisce un messaggio di stato.

Test case:

    Un gestore del cinema configura le sale aggiungendo i film e i dettagli dei posti.
    Un cliente sceglie un film e prenota un certo numero di posti.
    Il sistema verifica la disponibilità e conferma o rifiuta la prenotazione.

'''
# Svolgimento ES. Cinema:

class Film():

    def __init__(self, titolo: str, durata: float):

        self.titolo = titolo
        self.durata = durata

class Sala():

    def __init__(self, id: int, film_in_programmazione: Film, posti_totali: int, posti_prenotati: int = 0):

        self.id = id
        self.film_in_programmazione = film_in_programmazione
        self.posti_totali = posti_totali
        self.posti_prenotati = posti_prenotati


    def prenota_posti(self, num_posti: int):

        if self.posti_prenotati < self.posti_totali and self.posti_prenotati + num_posti < self.posti_totali:
            self.posti_prenotati += num_posti

            return f"Abbiamo ancora posti disponibili"
        
        elif self.posti_totali == num_posti + self.posti_prenotati:
            self.posti_prenotati += num_posti

            return f"Grazie della prenotazione.\nÈ sata raggiunta la capienza massima di {self.posti_totali} posti in sala"
        
        else:
            return "Mi dispiace ma i posti disponibili sono terminati "


    def posti_disponibili(self):
        return f"i posti disponibili sono: {self.posti_totali - self.posti_prenotati}"
    
class Cinema():
    
    def __init__(self):
        self.sale = []
       # self.film = []
    
    def aggiungi_sala(self, sala: Sala,):
        self.sale.append(sala)
        #self.film.append(sala.film_in_programmazione)
        
    def prenota_film(self, titolo_film: str, num_posti: int):
        if titolo_film == sala_rossa.film_in_programmazione or sala_blue.film_in_programmazione or sala_verde.film_in_programmazione:
            pass

            
                
Vois_Cinema = Cinema()

film1 = Film("Kill Bill Volume 1", 1.51)
film2 = Film("Shutter Island", 2.18)
film3 = Film("Oppenheimer", 3.00)

sala_rossa = Sala(id= 1, film_in_programmazione= film1, posti_totali= 100, posti_prenotati= 0)
sala_blue = Sala(id= 2, film_in_programmazione= film2, posti_totali= 100, posti_prenotati= 0)
sala_verde = Sala(id= 3, film_in_programmazione= film3, posti_totali= 100, posti_prenotati= 0)

Vois_Cinema.aggiungi_sala(sala_rossa)
Vois_Cinema.aggiungi_sala(sala_blue)
Vois_Cinema.aggiungi_sala(sala_verde)

print(Vois_Cinema.prenota_film("Oppenheimer", 23))









