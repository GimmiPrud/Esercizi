# Giammarco Prudenzi                      10/05/2024

# Esercizi lezione7:

# ES. 1:
'''
Scrivi una funzione che prenda un dizionario e un valore,
e ritorni la prima chiave che corrisponde a quel valore, o None se il valore non è presente.
'''
# Svolgimento ES. 1:

if False:

    def trova_chiave_per_valore(dizionario: dict[str: int], valore: int) -> str:

        for key,value in dizionario.items():
            if value == valore:
                return key

    print(trova_chiave_per_valore({'a': 100, 'b': 200, 'c': 300}, 200))
    print(trova_chiave_per_valore({'k1': 'v1', 'k2': 'v2'}, 'v3'))


# ES. 2:
'''
Scrivi una funzione che riceve una lista di numeri, filtra i numeri pari,
e restituisce una nuova lista con i numeri pari moltiplicati per un fattore dato.
'''
# Svolgimento ES. 2:

if False:

    def filtra_moltiplica(lista_numeri: list[int], fattore: int) -> list[int]:
        moltip_num = []
        for n in lista_numeri[:]:
            if n % 2 == 0:
                moltip_num.append(n* fattore)
        
        return moltip_num

    print(filtra_moltiplica([1, 2, 3, 4, 5, 6], 3))
    print(filtra_moltiplica([], 3))


# ES. 3:
'''
scrivi una funzione che elimini dalla lista dati certi elementi specificati in un dizionario.
Il dizionario contiene elementi da rimuovere come chiavi e il numero di volte che devono essere rimossi come valori.
'''
# Svolgimento ES. 3:

if False:
    def rimuovi_elementi(lista: list[int], da_rimuovere: dict[int:int]) -> list[int]:
        for k,v in da_rimuovere.items():
            for n in range(v):
                if k in lista:
                    lista.remove(v)
                    
        return lista
                
                
    print(rimuovi_elementi([1, 2, 3, 2, 4], {2: 2}))
    print(rimuovi_elementi([], {2:1})) 


# ES. 4:
'''
Scrivi una funzione che prenda in input una lista di dizionari che rappresentano voti di studenti 
aggrega i voti per studente in un nuovo dizionario.
'''
# Svolgimento ES. 4:

if False:

    def aggrega_voti(voti: list[dict]) -> dict[str:list[int]]:
        grade: dict = {}
        for voto in voti:
            nome = voto["nome"]
            v = voto['voto']
            if nome in grade:
                grade[nome].append(v)
            else:
                grade[nome]=[v]
        return grade

    print(aggrega_voti([{'nome': 'Alice', 'voto': 90}, {'nome': 'Bob', 'voto': 75}, {'nome': 'Alice', 'voto': 85}]))
    print(aggrega_voti([])) 


# ES. 5:
'''
Scrivi una funzione che accetti un dizionario di prodotti con i prezzi 
e restituisca un nuovo dizionario con solo i prodotti che hanno un prezzo superiore a 20, scontati del 10%
'''
# Svolgimento ES. 5:

if False:

    def filtra_e_mappa(prodotti: dict[str:float]) -> list[str:float]:
        sconto: dict = {}
        for k,v in prodotti.items():
            if v > 20:
                sconto[k] = v * 0.9
                
        return sconto

    print(filtra_e_mappa({'Penna': 15.0, 'Zaino': 50.0, 'Quaderno': 22.0}))
    print(filtra_e_mappa({'Gomma': 2.0, 'Matita': 1.0})) 


# ES. 6:
'''
PARTE 1
Scrivi una funzione chiamata create_contact() che accetta il nome e cognome, 
e-mail (facoltativo) e numero di telefono (facoltativo). La funzione dovrebbe restituire un dizionario con i dettagli del contatto.
 
PARTE 2
Scrivi una funzione chiamata update_contact() che accetta il dizionario creato, il nome e cognome del contatto da aggiornare,
 e il dettaglio facoltativo da aggiornare. Questa funzione dovrebbe aggiornare il dizionario del contatto
'''
# Svolgimento ES. 6:

if False:

    def create_contact(name: str, email: str=None, telefono: int=None) -> dict:

        info = {"name":name, "email": email, "telefono":telefono}
        return info 

    
    def update_contact(dictionary: dict, name: str, email: str =None, telefono: int=None) -> dict:

        if dictionary["name"] == name:
            if email:
                dictionary["email"] = email
            
            if telefono:
                dictionary["telefono"] = telefono

        return dictionary
        
    contact = create_contact("Mario Rossi", email="mario.rossi@gmail.com", telefono=788787)
    print(create_contact("Mario Rossi", email="mario.rossi@gmail.com", telefono=788787))
    print(update_contact(contact, "Mario Rossi", telefono=123456789))


# ES. 7:
'''
Scrivi una funzione che prenda in input una lista di dizionari che rappresentano voti di studenti e aggrega i voti per studente in un nuovo dizionario.
'''
# Svolgimento ES. 7:

if True:

    def voti_studenti(voti: list[dict])-> dict:
        voto_per_studente = {}
        for i in voti:
            studente = i["Studente"]
            voto = i["voti"]



    print(voti_studenti(voti= [{"Studente":"Alessio", "voti": [23,21,18]}, {"Studente":"Camilla", "voti":[28,27,30]}, {"Studente":"Luca","voti":[22,25,24]}]))


# ES. 8:
'''
Scrivi una funzione che elimini dalla lista dati certi elementi specificati in un dizionario.
Il dizionario contiene elementi da rimuovere come chiavi e il numero di volte che devono essere rimossi come valori.
'''
# Svolgimento ES.8:

# ES. 9:
'''
Scrivi una funzione che converta una lista di tuple (chiave, valore) in un dizionario.
Se la chiave è già presente, aggiungi il valore alla lista di valori già associata alla chiave.
'''
# Svolgimento ES.9:


# ES. 10:
'''
Scrivi una funzione che prende una lista di numeri e ritorna un dizionario che classifica i numeri in liste separate per numeri pari e dispari.
'''
# Svolgimento ES.10:

# ES. 11:
'''
Scrivi una funzione che converte una temperatura da gradi Celsius a Fahrenheit e viceversa a seconda del parametro.
Utilizza il concetto di parametri opzionali.
'''
# Svolgimento ES.11:


# ES. 12:
'''
Scrivi una funzione che somma tutti i numeri interi di una lista che sono maggiori di un dato valore intero definito threshold.
'''
# Svolgimento ES.12:

# ES. 13
'''
Scrivi una funzione che, data una lista, ritorni un dictionary che mappa ogni elemento alla sua frequenza nella lista.
'''
# Svolgimento ES.13:

# ES. 14:
'''
Scrivi una funzione che ritorna un dizionario che unisce due dizionari.
Se una chiave è presente in entrambi, somma i loro valori nel nuovo dizionario.
'''
# Svolgimento ES.14:


# ES. 15:
'''
Scrivi una funzione che, dato un insieme e una lista di numeri interi da rimuovere, ritorni un nuovo insieme senza i numeri specificati nella lista.
'''
# Svolgimento ES.15:

# ES. 16:
'''
Scrivi una funzione che ritorna il valore massimo, minimo e la media di una lista di numeri interi.
'''
# Svolgimento ES.16:

# ES. 17:
'''
Scrivi una funzione che calcola la media di una lista di numeri e ritorna il valore arrotondato all'intero più vicino.
'''
# Svolgimento ES.17:
 
# ES. 18:
'''
Scrivi una funzione che rimuove tutti i duplicati da una lista, contenente sia numeri che lettere, mantenendo l'ordine originale degli elementi.
'''
# Svolgimento ES.18:

# ES. 19:
''' 
Scrivi una funzione che ruota gli elementi di una lista verso sinistra di un numero specificato k di posizioni.
La rotazione verso sinistra significa che ciascun elemento della lista viene spostato a sinistra di una posizione e
l'elemento iniziale viene spostato alla fine della lista.
Per la rotazione utilizzare lo slicing e gestire il caso in cui il numero specificato di posizioni sia maggiore della lunghezza della lista.
'''
# Svolgimento ES.19:

# ES. 20: 
'''
Scrivi una funzione che accetti tre parametri: username, password e status di attivazione dell'account (attivo/non attivo).
L'accesso è consentito solo se il nome utente è "admin", la password corrisponde a "12345" e l'account è attivo.
'''
# Svolgimento ES.20:

# ES. 21: 
'''
Scrivi una funzione che verifica se una combinazione di condizioni (A, B, e C) è soddisfatta per procedere con un'operazione.
L'operazione può procedere solo se la condizione A è vera o se entrambe le condizioni B e C sono vere.
'''
# Svolgimento ES.21:

# ES. 22:
''' 
Scrivi una funzione che riceve un numero e stampa un conto alla rovescia da quel numero a zero.
'''
# Svolgimento ES.22:


# ES. 23:
''' 
Scrivi una funzione che, dato un numero intero, determina se è un "numero magico".
Un numero magico è definito come un numero che contiene il numero 7.
'''
# Svolgimento ES.23:
 
# ES. 24:
'''
Scrivi una funzione che verifica se in una stringa le parentesi '(' e ')'
sono bilanciate, cioè per ogni parentesi che apre c'è la corrispondente parentesi che chiude.
'''
# Svolgimento ES.24:

# ES. 25: 
'''
Scrivi una funzione che conta quante volte un elemento appare isolato in una lista di numeri interi.
Un elemento è considerato isolato se non è affiancato da elementi uguali.
'''
# Svolgimento ES.25:

# ES. 26:
'''
Scrivi una funzione chiamata create_contact() che accetta il nome e cognome, e-mail (facoltativo) e numero di telefono (facoltativo).
La funzione dovrebbe restituire un dizionario con i dettagli del contatto.

ESEMPIO: create_contact("Mario Rossi", email="mario.rossi@gmail.com", telefono=69876543)

OUTPUT: {'profile': 'Mario Rossi', 'email': 'mario.rossi@gmail.com', 'telefono': 788787}

Scrivi una funzione chiamata update_contact() che accetta il dizionario creato, il nome e cognome del contatto da aggiornare, e il dettaglio facoltativo da aggiornare. Questa funzione dovrebbe aggiornare il dizionario del contatto.

ESEMPIO: update_contact(dict, "Mario Rossi", telefono=123456789)

OUTPUT: {'profile': 'Mario Rossi', 'email': 'mario.rossi@gmail.com', 'telefono': 123456789}
'''
# Svolgimento ES.26: