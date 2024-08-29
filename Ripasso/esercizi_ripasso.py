# Giammarco Prudenzi 
'''
Sviluppa un sistema per la gestione dei contatti in Python che permetta agli utenti di creare, modificare, e cercare contatti basati sui numeri di telefono.
Il sistema dovrà essere capace di gestire una collezione (dizionario) di contatti e i loro numeri di telefono.

1. Classe ContactManager:
Gestisce tutte le operazioni legate ai contatti.
Attributi:
contacts: dict[str, list[str]] - Dizionario che ha per chiave il nome del contatto e per valore una lista di numeri di telefono. 
I numeri di telefono sono espressi sottoforma di stringa.
Metodi:
create_contact(name: str, phone_numbers: list[str]): Crea un nuovo contatto, aggiungendolo al dizionario contacts con il nome specificato e una lista di numeri di telefono.
Restituisce un nuovo dizionario con il solo contatto appena creato o il messaggio di errore "Errore: il contatto esiste già." se il contatto esiste già.
add_phone_number(contact_name: str, phone_number: str): Aggiunge un numero di telefono al contatto specificato. 
Restituisce un nuovo dizionario con il solo contatto aggiornato o i messaggi di errore "Errore: il contatto non esiste." se il contatto non esiste oppure "Errore: il numero di telefono esiste già." se il numero di telefono è già presente per il contatto specificato.
remove_phone_number(contact_name: str, phone_number: str): Rimuove un numero di telefono dal contatto specificato.
Restituisce un nuovo dizionario con il solo contatto aggiornato o i messaggi di errore "Errore: il contatto non esiste." se il contatto non esiste oppure "Errore: il numero di telefono non è presente." se il numero di telefono non esiste per il contatto specificato.
update_phone_number(contact_name: str, old_phone_number: str, new_phone_number: str): Sostituisce un numero di telefono con un altro nel contatto specificato. Restituisce un nuovo dizionario con il solo contatto aggiornato o i messaggi di errore "Errore: il contatto non esiste." se il contatto non esiste oppure "Errore: il numero di telefono non è presente." se il numero di telefono non esiste per il contatto specificato.
list_contacts(): Ritorna una lista di tutte le chiavi all'interno del dizionario contacts.
list_phone_numbers(contact_name: str): Mostra i numeri di telefono di un contatto specifico. 
Restituisce la lista dei numeri di telefono o il messaggio di errore "Errore: il contatto non esiste."
se il contatto non esiste.
search_contact_by_phone_number(phone_number: str): Trova e restituisce tutti i contatti che contengono un determinato numero di telefono.
Restituisce una lista di tutte le chiavi all'interno del dizionario contacts che hanno il numero specificato tra i valori oppure il messaggio di errore "Nessun contatto trovato con questo numero di telefono." se nessun contatto contiene il numero di telefono.
'''
if False:
    class ContactManager:
        def __init__(self):
            self.contacts: dict[str, list[str]] = {}
        
        def create_contact(self, name: str, phone_numbers: list[str]):
            pass
                 
        def add_phone_number(self, contact_name: str, phone_number: str):
            pass
            
        def remove_phone_number(self, contact_name: str, phone_number: str):
            pass
            
        def update_phone_number(self, contact_name: str, old_phone_number: str, new_phone_number: str):
            pass
                
                
                  
    manager = ContactManager()
    # Creazione di nuovi contatti
    print(manager.create_contact("Alice", ["123456789"]))
    print(manager.create_contact("Bob", ["987654321"]))
    print(manager.create_contact("Alice", ["111222333"]))

    # Aggiunta di numeri di telefono
    print(manager.add_phone_number("Alice", "111222333"))
    print(manager.add_phone_number("Charlie", "444555666"))
    print(manager.add_phone_number("Alice", "123456789"))
    # result
    '''
    {'Alice': ['123456789']}
    {'Bob': ['987654321']}
    Errore: il contatto esiste già.
    {'Alice': ['123456789', '111222333']}
    Errore: il contatto non esiste.
    Errore: il numero di telefono esiste già.
    # Creazione di un nuovo gestore di contatti
    '''
    
    manager = ContactManager()
    # Creazione di nuovi contatti
    print(manager.create_contact("Alice", ["123456789"]))
    print(manager.create_contact("Bob", ["987654321"]))
    print(manager.create_contact("Alice", ["111222333"]))
    # Rimozione di numeri di telefono
    print(manager.remove_phone_number("Alice", "111222333"))
    print(manager.remove_phone_number("Charlie", "444555666"))
    print(manager.remove_phone_number("Alice", "999999999"))
    # result 
    '''
    {'Alice': ['123456789']}
    {'Bob': ['987654321']}
    Errore: il contatto esiste già.
    Errore: il numero di telefono non è presente.
    Errore: il contatto non esiste.
    Errore: il numero di telefono non è presente.
    '''
#-------------------------------------------------------------------------#

'''
Si scriva una funzione in Python che simuli una palla che rimbalza calcolando la sua altezza da terra in centimetri per ogni secondo,
a mano a mano che il tempo passa su un orologio simulato.

Al tempo zero la palla comincia ad altezza zero e ha una velocità iniziale di 100 cm/s.

Dopo ogni secondo, il valore dell'altezza cambia, aggiungendo al valore corrente dell'altezza il valore della velocità corrente;
poi, il valore della velocità viene modificato, sottraendo 96 al valore della velocità corrente.
Dunque, dopo ogni secondo, si ha che
altezza = altezza + velocità
velocità = velocità - 96.
 
Se il nuovo valore che si ottiene per l'altezza è inferiore a 0,
si deve moltiplicare altezza e velocità per -0.5 per simulare il rimbalzo. Dunque, per il rimbalzo, si avrà che
altezza= altezza*-0,5 
velocità=velocità*-0,5.

Ci si fermi al quinto rimbalzo.
 
Per ogni secondo, la funzione deve stampare il tempo trascorso e l'altezza a cui si trova la palla in quel determinato secondo.
Ad esempio, se al tempo 0, la palla si trova ad altezza 0 cm, allora la funzione stamperà:
 
"Tempo: 0 Altezza: 0"
 
Se avviene il rimbalzo, la funzione deve stampare il tempo trascorso e la parola "Rimbalzo!".
Ad esempio, se il rimbalzo avviene al tempo 4, allora la funzione stamperà:
 
"Tempo: 4 Rimbalzo!"
'''
if True:
    
    def rimbalzo() -> None:

        tempo: int = 0
        altezza: float = 0.0
        velocita: float = 100.0
        rimbalzi: int = 0
        
    # Result
    '''
    rimbalzo()
    Tempo: 0 Altezza: 0.0
    Tempo: 1 Altezza: 100.0
    Tempo: 2 Altezza: 104.0
    Tempo: 3 Altezza: 12.0
    Tempo: 4 Rimbalzo!
    Tempo: 5 Altezza: 88.0
    Tempo: 6 Altezza: 230.0
    Tempo: 7 Altezza: 276.0
    Tempo: 8 Altezza: 226.0
    Tempo: 9 Altezza: 80.0
    Tempo: 10 Rimbalzo!
    Tempo: 11 Altezza: 81.0
    Tempo: 12 Altezza: 250.0
    Tempo: 13 Altezza: 323.0
    Tempo: 14 Altezza: 300.0
    Tempo: 15 Altezza: 181.0
    Tempo: 16 Rimbalzo!
    Tempo: 17 Altezza: 17.0
    Tempo: 18 Altezza: 172.5
    Tempo: 19 Altezza: 232.0
    Tempo: 20 Altezza: 195.5
    Tempo: 21 Altezza: 63.0
    Tempo: 22 Rimbalzo!
    Tempo: 23 Altezza: 82.75
    Tempo: 24 Altezza: 245.0
    Tempo: 25 Altezza: 311.25
    Tempo: 26 Altezza: 281.5
    Tempo: 27 Altezza: 155.75
    Tempo: 28 Rimbalzo!
    '''
    
    
    

        
        
        
    

