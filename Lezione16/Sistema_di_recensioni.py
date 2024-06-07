
# Giammarco Prudenzi 
# Esercizi sulle funzioni 

# Sistema di recensioni:

'''
Implementare una classe Media che rappresenti un media generico (ad esempio, un film o un libro) e una classe derivata Film che rappresenti specificamente un film.
Gli studenti dovranno anche creare oggetti di queste classi, aggiungere valutazioni e visualizzare le recensioni.

Specifiche della Classe Media:
 
Attributi:
- title (stringa): Il titolo del media.
- reviews (lista di interi): Una lista di valutazioni del media, con voti compresi tra 1 e 5.

Metodi:
- set_title(self, title): Imposta il titolo del media.
- get_title(self): Restituisce il titolo del media.
- aggiungiValutazione(self, voto): Aggiunge una valutazione alla lista delle recensioni se è valida (tra 1 e 5).
- getMedia(self): Calcola e restituisce la media delle valutazioni.
- getRate(self): Restituisce una stringa che descrive il giudizio medio basato sulla media delle valutazioni,
  ovvero mostra "Terribile" se il voto medio si avvicina a 1,
 "Brutto" se il voto medio si avvicina a 2,
 "Normale" se il voto medio si avvicina a 3, "Bello" se il voto medio si avvicina a 4, "Grandioso" se il voto medio si avvicina a 5.
- ratePercentage(self, voto): Calcola e restituisce la percentuale di un voto specifico nelle recensioni.
- recensione(self): Mostra un riassunto delle recensioni e delle valutazioni del media, 
  stampando il titolo, il voto medio, il giudizio e le percentuali di ciascun voto. Esempio di riassunto:
 
Titolo del Film: The Shawshank Redemption
Voto Medio: 3.80
Giudizio: Bello
Terribile: 10.00%
Brutto: 10.00%
Normale: 10.00%
Bello: 30.00%
Grandioso: 40.00%

Si verifichi il funzionamento scrivendo un codice che crei almeno due oggetti di tipo Film,
aggiunga a ognuno dei due almeno dieci valutazioni e richiami il metodo recensione().

'''
# Svolgimento ES. Sistema di recensioni:

class Media:

    def __init__(self, title: str, reviews = []):

        self.title = title
        self.reviews = reviews

    def set_title(self, title):
        self.title = title
    
    def get_title(self):
        return f"Titolo film: {self.title}"
    
    def aggiungiValutazione(self, voto):
        if 1 <= voto <= 5 :
            self.reviews.append(voto)
        else:
            pass

    def getMedia(self):
        sum = 0
        for i in self.reviews:
            sum += i
        return f"Voto medio: {sum/len(self.reviews)}"

    def getRate(self):
        sum = 0
        for i in self.reviews:
            sum += i
        x = round(sum/len(self.reviews),2)

        if 0 <= x <= 1:
            return "Giudizio: Terribile"
        elif 1 < x <= 2:
            return "Giudizio: Brutto"
        elif 2 < x <= 3:
            return "Giudizio: Normale"
        elif 3 < x <= 4:
            return "Giudizio: Bello"
        else:
            return "Giudizio: Grandioso"
        
    def ratePercentage(self, voto):
        count = self.reviews.count(voto)
        perc = (count / len(self.reviews)) *100  
        
        return f"{perc} %"

    def recensione(self):
        print(self.title)
        print(self.getMedia())
        print(self.getRate())
        for i in set(self.reviews):
            if 0 <= i <= 1:
                print(f"Terribile: {self.ratePercentage(i)}")
            elif 1 < i <= 2:
                print(f"Brutto: {self.ratePercentage(i)}")
            elif 2 < i <= 3:
                print(f"Normale: {self.ratePercentage(i)}")
            elif 3 < i <= 4:
                print(f"Bello: {self.ratePercentage(i)}")
            elif 4 < i < 5:
                print(f"Grandioso: {self.ratePercentage(i)}")
            
class Film(Media):

    def __init__(self, title: str, reviews=[]):
        super().__init__(title, reviews)
        


American_Psycho = Film(title="American Psycho",reviews=[])
Il_Padrino = Film(title="Il Padrino",reviews=[])

#print(American_Psycho.get_title())
#print(Il_Padrino.get_title())

American_Psycho.aggiungiValutazione(2)
American_Psycho.aggiungiValutazione(4)
American_Psycho.aggiungiValutazione(3)
American_Psycho.aggiungiValutazione(3)
American_Psycho.aggiungiValutazione(4)

Il_Padrino.aggiungiValutazione(5)
Il_Padrino.aggiungiValutazione(4)
Il_Padrino.aggiungiValutazione(4.5)
Il_Padrino.aggiungiValutazione(4.5)
Il_Padrino.aggiungiValutazione(4.5)

# print(American_Psycho.getMedia())
# print(Il_Padrino.getMedia())

# print(American_Psycho.getRate())
# print(Il_Padrino.getRate())

# print(American_Psycho.ratePercentage(4))
# print(Il_Padrino.ratePercentage(4.5))

Il_Padrino.recensione()
print("-"*20)
American_Psycho.recensione()


