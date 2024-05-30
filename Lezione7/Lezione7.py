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

