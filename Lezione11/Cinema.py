
# Giammarco Prudenzi 

# Esercizi sulle classi:

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

    def __init__(self, id: int, film_in_programmazione: str, posti_totali: int, posti_prenotati: int = 0):

        self.id = id
        self.film_in_programmazione = film_in_programmazione
        self.posti_totali = posti_totali
        self.posti_prenotati = posti_prenotati


    def prenota_posti(self, num_posti: int):

        while self.posti_prenotati <= self. posti_totali:
            self.posti_prenotati += num_posti

            if self.posti_prenotati < self.posti_totali:
                self.posti_totali -= self.posti_prenotati
                return "Ciao, abbiamo ancora dei posti disponibili"
            else:
                print("Mi dispiace ma abbiamo finito i posti ")
            break
            

    def posti_disponibili(self):
        posti_dispo = self.posti_prenotati - self.posti_prenotati
        return f"Sono ancora disponibili {posti_dispo} posti in questa sala"
    

sala_rossa = Sala(id= 203, film_in_programmazione= "King Kong",posti_totali= 100, posti_prenotati= 0)

''''
class Cinema():

    def __init__(self,):
        pass

    def aggiungi_sala(self, sala: Sala):
        pass

    def prenota_film(self, titolo_film: str, num_posti: int):
        pass
'''





