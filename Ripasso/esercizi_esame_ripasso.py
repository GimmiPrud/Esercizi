'''
Scrivi una funzione che converta una lista di tuple (chiave, valore) in un dizionario. 
Se la chiave è già presente, aggiungi il valore alla lista di valori già associata alla chiave.
'''
if False:

    def lista_a_dizionario(tuples: tuple) -> dict[str:list[int]]:
        dizio = {}
        for i,v in tuples:
            if i in dizio:
                dizio[i].append(v)
            else:
                dizio[i] = [v]
        return dizio
    """
        for i in tuples:
            if i[0] not in dizio.keys():
                dizio[i[0]]=[i[1]]
            else:
                dizio[i[0]].append(i[1])
        return dizio
    """

    print(lista_a_dizionario([('a', 1), ('b', 2), ('a', 3)])) # result {'a': [1, 3], 'b': [2]}
    print(lista_a_dizionario([])) # result {}

#------------------------------------------------------------------------------------------#
'''
Scrivi una funzione che verifica se una combinazione di condizioni (A, B, e C) è soddisfatta per procedere con un'operazione.
L'operazione può procedere solo se la condizione A è vera o se entrambe le condizioni B e C sono vere.
La funzione deve ritornare "Operazione permessa" oppure "Operazione negata" a seconda delle condizioni che sono soddisfatte.
'''
if False:

    def check_combination(conditionA: bool, conditionB: bool, conditionC: bool) -> str:
        if conditionA == True or conditionB and conditionC == True:
            return "operazione permessa"
        else:
            return "operazione negata"

    print(check_combination(True, False, True)) # result -> Operazione permessa
    print(check_combination(False, True, False)) # result -> Operazione negata

#----------------------------------------------------------------------------------------#
'''
Scrivi una funzione che, data una lista, ritorni un dictionary che mappa ogni elemento alla sua frequenza nella lista.
'''
if False:

    def frequency_dict(elements: list) -> dict:
        frutta = {}
        for i in elements:
            if i in elements:
                frutta[i]= elements.count(i)
        return frutta

    print(frequency_dict(['mela', 'banana', 'mela'])) # result {'mela': 2, 'banana': 1}

#-------------------------------------------------------------------------------------------#
'''
Scrivi una funzione che prenda un dizionario e un valore, e ritorni la prima chiave che corrisponde a quel valore, o None se il valore non è presente.
'''
if False:

    def trova_chiave_per_valore(dizionario: dict[str: int], valore: int) -> str:
        for k,v in dizionario.items():
            if v == valore:
                return k
            
    print(trova_chiave_per_valore({'a': 100, 'b': 200, 'c': 300}, 200)) # result b
    print(trova_chiave_per_valore({'k1': 'v1', 'k2': 'v2'}, 'v3')) # result None

#---------------------------------------------------------------------------------------------#

'''
Progettare un sistema di videonoleggio con i seguenti requisiti:

1. Classe Movie:

Attributi:
    movie_id: str - Identificatore di un film.
    title: str - Titolo del film.
    director: str - Regista del film.
    is_rented: boolean - Booleano che indica se il film è noleggiato o meno.

Metodi:
    rent(): Contrassegna il film come noleggiato se non è già noleggiato.
    Se il film non è già noleggiato imposta is_rented a True, altrimenti stampa il messaggio "Il film {self.title} è già noleggiato."
    return_movie(): Contrassegna il film come restituito.
    Se il film è già noleggiato imposta is_rented a False, altrimenti stampa il messaggio "Il film {self.title} non è attualmente noleggiato."

2. Classe Customer:

Attributi:
    customer_id: str - Identificativo del cliente.
    name: str - Nome del cliente.
    rented_movies: list[Movie] - Lista dei film noleggiati.

Metodi:
    rent_movie(movie: Movie): Aggiunge il film nella lista rented_movies se non è già stato noleggiato,
    altrimenti stampa il messaggio "Il film {movie.title} è già noleggiato."
    return_movie(movie: Movie): Rimuove il film dalla lista rented_movies se già presente,
    altrimenti stampa il messaggio "Il film {movie.title} non è stato noleggiato da questo cliente."

3. Classe VideoRentalStore:

Attributi:
    movies: dict[str, Movie] - Dizionario che ha per chiave l'id del film e per valore l'oggetto Movie.
    customers: dict[str, Customer] - Dizionario che ha per chiave l'id del cliente e per valore l'oggetto Customer.

Metodi:
    add_movie(movie_id: str, title: str, director: str): Aggiunge un nuovo film nel videonoleggio se non è già presente,
    altrimenti stampa il messaggio "Il film con ID {movie_id} esiste già."
    register_customer(customer_id: str, name: str): Iscrive un nuovo cliente nel videonoleggio se non è già presente,
    altrimenti stampa il messaggio "Il cliente con ID {customer_id} è già registrato."
    rent_movie(customer_id: str, movie_id: str): Permette al cliente di noleggiare un film se entrambi esistono nel videonoleggio,
    altrimenti stampa il messaggio "Cliente o film non trovato."
    return_movie(customer_id: str, movie_id: str): Permette al cliente di restituire un film se entrambi esistono nel videonoleggio,
    altrimenti stampa il messaggio "Cliente o film non trovato."
    get_rented_movies(customer_id: str): list[Movie] - Restituisce la lista dei film noleggiati dal client (customer.rented_movies) se 
    il cliente esiste nel videonoleggio, altrimenti stampa il messaggio "Cliente non trovato." e ritorna una lista vuota.
'''
if False:
    class Movie:
        def __init__(self, movie_id: str, title: str, director: str, is_rended: bool):
            self.movie_id = movie_id
            self.title = title
            self.director = director
            self.is_rended = is_rended
        
        def rent(self):
            if self.is_rended == False:
                self.is_rended = True
            else:
                return f"Il film {self.title} è già noleggiato."

        def return_movie(self):
            if self.is_rended == True:
                self.is_rended = False
            else:
                return f"Il film {self.title} non è attualmente noleggiato."


    class Customer:
        def __init__(self, customer_id: str, name: str, rented_movies: list[Movie]):
            self.customer_id = customer_id
            self.name = name
            self.rended_movies = rented_movies
            rented_movies = []

        def rent_movie(self, movie: Movie):
            if movie in self.rended_movies:
                return f"Il film {movie.title} è già noleggiato."
            else:
                self.rended_movies.append(movie)

        def return_movie(self, movie: Movie):
            if movie in self.rended_movies:
                self.rended_movies.remove(movie)
            else:
                return f"Il film {movie.title} non è stato noleggiato da questo cliente."

    class VideoRentalStore:
        def __init__(self, movies: dict[str, Movie], customers: dict[str, Customer]):
            self.movies = movies
            self.customers = customers


    videonoleggio = VideoRentalStore()
    # aggiunta nuovi film
    videonoleggio.add_movie("1", "Inception", "Christopher Nolan")
    videonoleggio.add_movie("2", "The Matrix", "Wachowski Brothers")
    # Registrazione di nuovi clienti
    videonoleggio.register_customer("101", "Alice")
    videonoleggio.register_customer("102", "Bob")
    # Noleggio di film
    videonoleggio.rent_movie("101", "1")
    videonoleggio.rent_movie("102", "2")
    # Tentativo di noleggiare un film già noleggiato
    videonoleggio.rent_movie("101", "1")
    # Restituzione di film
    videonoleggio.return_movie("101", "1")
    # Tentativo di restituire un film non noleggiato
    videonoleggio.return_movie("101", "1")
    # Ottenere la lista dei film noleggiati da un cliente
    rented_movies_alice = videonoleggio.get_rented_movies("101")
    print(f"Film noleggiati da Alice: {[movie.title for movie in rented_movies_alice]}")
    rented_movies_bob = videonoleggio.get_rented_movies("102")
    print(f"Film noleggiati da Bob: {[movie.title for movie in rented_movies_bob]}")

#---------------------------------------------------------------------------------------#
'''
Scrivi una funzione che accetti un dizionario di prodotti con i prezzi e
restituisca un nuovo dizionario con solo i prodotti che hanno un prezzo superiore a 20, scontati del 10%.
'''
if False:
    def filtra_e_mappa(prodotti: dict[str:float]) -> dict[str:float]:
        prod_scont = {}
        for k,v in prodotti.items():
            if v > 20:
                prod_scont[k] = v*0.9
        return prod_scont

    print(filtra_e_mappa({'Penna': 15.0, 'Zaino': 50.0, 'Quaderno': 22.0})) # result {'Zaino': 45.0, 'Quaderno': 19.8}
    print(filtra_e_mappa({'Gomma': 2.0, 'Matita': 1.0})) # result {}

#--------------------------------------------------------------------------------------#
'''
1. Classe Base: Veicolo
Crea una classe base chiamata Veicolo con i seguenti attributi e metodi:
 
Attributi:
- marca (stringa)
- modello (stringa)
- anno (intero)

Metodi:
- __init__(self, marca, modello, anno): metodo costruttore che inizializza gli attributi marca, modello e anno.
- descrivi_veicolo(self): metodo che stampa una descrizione del veicolo nel formato "Marca: [marca], Modello: [modello], Anno: [anno]".

2. Classe Derivata: Auto
Crea una classe derivata chiamata Auto che eredita dalla classe Veicolo e aggiunge i seguenti attributi e metodi:
 
Attributi:
- numero_porte (intero)

Metodi:
- __init__(self, marca, modello, anno, numero_porte): metodo costruttore che inizializza gli attributi della classe base e numero_porte.
- descrivi_veicolo(self): metodo che sovrascrive quello della classe base per includere anche il -
 numero di porte nella descrizione, nel formato "Marca: [marca], Modello: [modello], Anno: [anno], Numero di porte: [numero_porte]".

3. Classe Derivata: Moto
Crea una classe derivata chiamata Moto che eredita dalla classe Veicolo e aggiunge i seguenti attributi e metodi:
 
Attributi:
- tipo (stringa, ad esempio "sportiva", "cruiser", ecc.)

Metodi:
- __init__(self, marca, modello, anno, tipo): metodo costruttore che inizializza gli attributi della classe base e tipo.
- descrivi_veicolo(self): metodo che sovrascrive quello della classe base per includere anche il tipo di moto nella descrizione,
nel formato "Marca: [marca], Modello: [modello], Anno: [anno], Tipo: [tipo]".
'''
if False:
    class Veicolo:
        def __init__(self, marca: str, modello: str, anno: int):
            self.marca = marca
            self.modello = modello
            self.anno = anno

        def descrivi_veicolo(self):
            print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}")
        
    class Auto(Veicolo):
        def __init__(self, marca: str, modello: str, anno: int, numero_porte: int):
            super().__init__(marca, modello, anno)
            self.numero_porte = numero_porte

        def descrivi_veicolo(self):
            print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}, Numero di porte: {self.numero_porte}")
        
    class Moto(Veicolo):
        def __init__(self, marca: str, modello: str, anno: int, tipo: str):
            super().__init__(marca, modello, anno)
            self.tipo = tipo
        
        def descrivi_veicolo(self):
            print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}, Tipo: {self.tipo}")
            

    veicolo = Veicolo("Generic", "Model", 2020)  # Crea un'istanza della classe Veicolo
    auto = Auto("Toyota", "Corolla", 2021, 4)  # Crea un'istanza della classe Auto
    moto = Moto("Yamaha", "R1", 2022, "sportiva")  # Crea un'istanza della classe Moto
    veicolo.descrivi_veicolo()  # Test del metodo descrivi_veicolo per Veicolo
    auto.descrivi_veicolo()  # Test del metodo descrivi_veicolo per Auto
    moto.descrivi_veicolo()  # Test del metodo descrivi_veicolo per Moto
    # Test case aggiuntivi
    veicolo = Veicolo("Generic", "Model", 2020)  # Crea un'istanza della classe Veicolo
    auto2 = Auto("Honda", "Civic", 2019, 5)  # Crea un'altra istanza della classe Auto
    moto2 = Moto("Ducati", "Panigale", 2023, "superbike")  # Crea un'altra istanza della classe Moto
    # Verifica che le descrizioni siano corrette
    veicolo.descrivi_veicolo()  # Test del metodo descrivi_veicolo per Veicolo
    auto2.descrivi_veicolo()  # Test del metodo descrivi_veicolo per una seconda Auto
    moto2.descrivi_veicolo()

#----------------------------------------------------------------------#
'''
Scrivi una funzione che prende una lista di numeri e ritorna un dizionario che classifica i numeri in liste separate per numeri pari e dispari.
'''
if False:
    def classifica_numeri(lista: int) -> dict[str:list[int]]:
        n_pari_dispari = {}
        pari = []
        dispari =[]
        for i in lista :
            if i % 2 == 0:
                pari.append(i)
            else:
                dispari.append(i)
        n_pari_dispari["pari"] = pari
        n_pari_dispari["dispari"] = dispari
        return n_pari_dispari


    print(classifica_numeri([1, 2, 3, 4, 5, 6])) 
    # {'pari': [2, 4, 6], 'dispari': [1, 3, 5]}
    print(classifica_numeri([]))
    #{'pari': [], 'dispari': []}

#--------------------------------------------------------------------#
'''
Scrivi una funzione che somma tutti i numeri interi di una lista che sono maggiori di un dato valore intero definito threshold.
'''
if False:
    def sum_above_threshold(numbers: list[int], threshold: int ) -> int:
        somma = 0
        for n in numbers:
            if n > threshold:
                somma += n
        return somma

    print(sum_above_threshold([15, 5, 25], 20)) # 25

#-------------------------------------------------------------------#
'''
Sviluppa un sistema per la gestione delle ricette in Python che permetta agli utenti di creare, modificare, e cercare ricette basate sugli ingredienti.
Il sistema dovrà essere capace di gestire una collezione (dizionario) di ricette e i loro ingredienti.

Classe:
- RecipeManager:
    Gestisce tutte le operazioni legate alle ricette.

    Metodi:
    - create_recipe(name, ingredients): Crea una nuova ricetta con il nome specificato e una lista di ingredienti.
    Restituisce un nuovo dizionario con la sola ricetta appena creata o un messaggio di errore se la ricetta esiste già.

    - add_ingredient(recipe_name, ingredient): Aggiunge un ingrediente alla ricetta specificata.
    Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente esiste già o la ricetta non esiste.

    - remove_ingredient(recipe_name, ingredient): Rimuove un ingrediente dalla ricetta specificata. 
    Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente non è presente o la ricetta non esiste.

    - update_ingredient(recipe_name, old_ingredient, new_ingredient): Sostituisce un ingrediente con un altro nella ricetta specificata. 
    Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente non è presente o la ricetta non esiste.

    - list_recipes(): Elenca tutte le ricette esistenti.

    - list_ingredients(recipe_name): Mostra gli ingredienti di una specifica ricetta.
    Restituisce un elenco di ingredienti o un messaggio di errore se la ricetta non esiste.

    - search_recipe_by_ingredient(ingredient): Trova e restituisce tutte le ricette che contengono un determinato ingrediente.
    Restituisce un elenco di ricette o un messaggio di errore se nessuna ricetta contiene l'ingrediente.
'''
if False:
    class RecipeManager:
        def __init__(self):
            self.recipe = {}

        def create_recipe(self, name, ingredients):
            if name in self.recipe:
                return "La ricetta esiste già."
            else:
                self.recipe[name] = ingredients
                return self.recipe

        def add_ingredient(self, recipe_name, ingredient):
            if recipe_name not in self.recipe:
                return "La ricetta non esiste."
            if ingredient in self.recipe[recipe_name]:
                return "L'ingrediente esiste già"
            else:
                self.recipe[recipe_name].append(ingredient)
                return self.recipe

        def remove_ingredient(self, recipe_name, ingredient):
            if recipe_name not in self.recipe:
                return "La ricetta non esiste."
            if ingredient not in self.recipe[recipe_name]:
                return "L'ingrediente non è presente"
            else:
                self.recipe[recipe_name].remove(ingredient)
                return self.recipe

        def update_ingredient(self, recipe_name, old_ingredient, new_ingredient):
            if recipe_name not in self.recipe:
                return "La ricetta non esiste."
            if old_ingredient not in self.recipe[recipe_name]:
                return "L'ingrediente da sostituire non è presente"
            else:
                self.recipe[recipe_name].remove(old_ingredient)
                self.recipe[recipe_name].append(new_ingredient)
                return self.recipe

        def list_recipes(self):
            lista = []
            for k in self.recipe:
                lista.append(k)
            return lista

        def list_ingredients(self, recipe_name):
            if recipe_name not in self.recipe:
                return "La ricetta non esiste."
            return self.recipe[recipe_name]

        def search_recipe_by_ingredient(self, ingredient):
            recipes= []
            for k,v in self.recipe.items():
                if v in self.recipe.values():
                    recipes.append(k)
            if not recipes:
                return "Nessuna ricetta contiene l'ingrediente specificato."
            return self.recipe
        
    manager = RecipeManager()

    print(manager.create_recipe("Pizza Margherita", ["Farina", "Acqua", "Lievito", "Pomodoro", "Mozzarella"]))
    print(manager.add_ingredient("Pizza Margherita", "Basilico"))
    print(manager.update_ingredient("Pizza Margherita", "Mozzarella", "Mozzarella di Bufala"))
    print(manager.remove_ingredient("Pizza Margherita", "Acqua"))
    print(manager.list_ingredients("Pizza Margherita"))
    
# result:
'''
{'Pizza Margherita': ['Farina', 'Acqua', 'Lievito', 'Pomodoro', 'Mozzarella']}
{'Pizza Margherita': ['Farina', 'Acqua', 'Lievito', 'Pomodoro', 'Mozzarella', 'Basilico']}
{'Pizza Margherita': ['Farina', 'Acqua', 'Lievito', 'Pomodoro', 'Mozzarella di Bufala', 'Basilico']}
{'Pizza Margherita': ['Farina', 'Lievito', 'Pomodoro', 'Mozzarella di Bufala', 'Basilico']}
['Farina', 'Lievito', 'Pomodoro', 'Mozzarella di Bufala', 'Basilico']
'''


#---------------------------------------------------------------------------#
'''
Scrivi una funzione che unisce due dizionari. Se una chiave è presente in entrambi, somma i loro valori. DA FINIRE!!!!
'''
if False:
    def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
        merged_dict = {}
        for key,value in dict1.items():
            if key in dict2:
                merged_dict[key]= value + dict2[key]
            else:
                merged_dict[key] = value    
        for key,value in dict2.items():
            if key not in dict1:
                merged_dict[key]= value 
        return merged_dict


    print(merge_dictionaries({'x': 5}, {'x': -5})) # result {'x': 0}
    print(merge_dictionaries({'a': 1, 'b': 2}, {'b': 3, 'c': 4})) # {'a': 1, 'b': 5, 'c': 4}
    print(merge_dictionaries({}, {'a': 10, 'b': 20}))    # {'a': 10, 'b': 20}
    print(merge_dictionaries({'x': 5}, {'x': -5}))
    print(merge_dictionaries({}, {}))
    print(merge_dictionaries({'a': 3}, {'b': 4}))

#------------------------------------------------------------------------#
'''
Progettare un semplice sistema bancario con i seguenti requisiti:

Classe del Account:
    Attributi:
    account_id: str - identificatore univoco per l'account.
    balance: float - il saldo attuale del conto.
    Metodi:
    deposit(amount: float) - aggiunge l'importo specificato al saldo del conto.
    get_balance(): restituisce il saldo corrente del conto.
Classe Bank:
    Attributi:
    accounts: dict[str, Account] - un dizionario per memorizzare gli account in base ai loro ID.
    Metodi:
    create_account(account_id): crea un nuovo account con l'ID specificato e un saldo pari a 0.
    deposit(account_id, amount): deposita l'importo specificato sul conto con l'ID fornito.
    get_balance(account_id): restituisce il saldo del conto con l'ID specificato.
'''
if False:
    class Account:
        def __init__(self, account_id: str):
            self.account_id = account_id
            self.balance:float = 0.0

        def deposit(self, amount: float):
            self.balance += amount

        def get_balance(self):
            return int(self.balance)
        
    class Bank:
        def __init__(self):
            self.accounts: dict[str,Account] = {}
        
        def create_account(self, account_id):
            if account_id not in self.accounts.keys():
                self.accounts[account_id] = Account(account_id)
            else:
                print("Account whit this ID already exists")
            return self.accounts[account_id]

        def deposit(self, account_id, amount):
            if account_id in self.accounts.keys():
                self.accounts[account_id].deposit(amount)

        def get_balance(self, account_id):
            if account_id in self.accounts.keys():
                return self.accounts[account_id].get_balance()
            else:
                print(" Account not found")

    bank = Bank()
    account1 = bank.create_account("123")
    print(account1.get_balance())
    # result 0
    bank = Bank()
    account1 = bank.create_account("123")
    bank.deposit("123",100)
    print(bank.get_balance("123"))
    # result 100
    bank = Bank()
    account2 = bank.create_account("456")
    bank.deposit("456",200)
    print(bank.get_balance("456"))
    # result 200
        

#-----------------------------------------------------------#
'''
Progettare un sistema di gestione della biblioteca con i seguenti requisiti:
Classe Book:
Attributi:
    book_id: str - Identificatore di un libro.
    title: str - titolo del libro.
    author: str - autore del libro
    is_borrowed: boolean - booleano che indica se il libro è in prestito o meno.
Metodi:
    borrow()-Contrassegna il libro come preso in prestito se non è già preso in prestito.
    return_book()- Contrassegna il libro come restituito.

Classe Member:
Attributi:
    member_id: str - identificativo del membro.
    name: str - il nome del membro.
    borrowed_books: list[Book] - lista dei libri presi in prestito.
Metodi:
    borrow_book(book): aggiunge il libro nella lista borrowed_books se non è già stato preso in prestito.
    return_book(book): rimuove il libro dalla lista borrowed_books.

Classe Library:
Attributi:
    books: dict[str, Book] - dizionario che ha per chiave l'id del libro e per valore l'oggetto Book
    members: dict[str, Member] - dizionario che ha per chiave l'id del membro e per valore l'oggetto Membro
Metodi:
    add_book(book_id: str, title: str, author: str): Aggiunge un nuovo libro nella biblioteca.
    register_member(member_id:str, name: str): Iscrive un nuovo membro nella biblioteca.
    borrow_book(member_id: str, book_id: str): Permette al membro di prendere in prestito il libro.
    return_book(member_id: str, book_id: str): Permette al membro di restituire il libro.
    get_borrowed_books(member_id): list[Book] - restituisce la lista dei libri presi in prestito dal membro.
'''
if False:
    class Book:
        def __init__(self, book_id: str, title: str, author: str):
            self.book_id = book_id
            self.title = title
            self.author = author
            self.is_borrowed = False
        
        def borrow(self):
            self.is_borrowed = True

        def return_book(self):
            self.is_borrowed = False
            
    class Member:
        def __init__(self, member_id: str, name: str):
            self.member_id = member_id
            self.name = name
            self.borrowed_books: list[Book] = []

        def borrow_book(self, book: Book):
            if book.book_id not in self.borrowed_books:
                self.borrowed_books.append(book)    

        def return_book(self, book: Book):
            if book.book_id in self.borrowed_books:
                self.borrowed_books.remove(book)
                
    class Library:
        def __init__(self):
            self.books: dict[str, Book] = {}
            self.members: dict[str, Member] = {}

        def add_book(self, book_id: str, title: str, author: str): 
            if book_id not in self.books.keys():
                self.books[book_id] = Book(book_id,title,author)

        def register_member(self, member_id:str, name: str):
            if member_id not in self.members.keys():
                self.members[member_id] = Member(member_id,name)

        def borrow_book(self, member_id: str, book_id: str): 
            if member_id in self.members.keys() and book_id in self.books.keys():
                self.members[member_id].borrow_book(self.books[book_id])
                
        def return_book(self, member_id: str, book_id: str): 
            if member_id in self.members and book_id in self.books:
                self.members[member_id].return_book(self.books[book_id])

        def get_borrowed_books(self, member_id):
            if member_id in self.members:
                return self.members[member_id].borrowed_books
        
    library = Library()

    library.add_book("B001", "The Great Gatsby", "F. Scott Fitzgerald")
    library.add_book("B002", "1984", "George Orwell")
    library.add_book("B003", "To Kill a Mockingbird", "Harper Lee")
    # Register members
    library.register_member("M001", "Alice")
    library.register_member("M002", "Bob")
    library.register_member("M003", "Charlie")
    # Borrow books
    library.borrow_book("M001", "B001")
    library.borrow_book("M002", "B002")
    
    print(library.get_borrowed_books("M001"))  # Expected output: ['The Great Gatsby']
    print(library.get_borrowed_books("M002"))  # Expected output: ['1984']

#--------------------------------------------------------------------#
'''
Scrivere il frammento di codice che cambi il valore intero memorizzato nella variabile x nel seguente modo:
- se x è pari, deve essere diviso per 2;
- se x è dispari deve essere moltiplicato per 3 e gli deve essere sottratto 1.
'''
if False:

    def transform(x: int) -> int:
        if x % 2 == 0:
            return x / 2
        else:
            return x * 3 -1

    print(transform(4))
    print(transform(-10))

#-------------------------------------------------------------------------#
'''
Scrivi una funzione che accetti tre parametri: username, password e status di attivazione dell'account (attivo/non attivo).
L'accesso è consentito solo se il nome utente è "admin", la password corrisponde a "12345" e l'account è attivo.
La funzione ritorna "Accesso consentito" oppure "Accesso negato".
'''
if False:
    def check_access(username: str, password: str, is_active: bool) -> str:
        if username == "admin" and password == "12345" and is_active == True:
            return "Accesso consentito"
        else: 
            return "Accesso negato"



# Esercizio esame python teorico:
'''
Progettare un semplice sistema di gestione di studenti e corsi con i seguenti requisiti:

1. Classe Student:
Attributi:
student_id: str - identificatore univoco per lo studente.
courses: list[str] - la lista dei corsi ai quali lo studente è iscritto.
Metodi:
enroll(course: str)-aggiunge il corso specificato alla lista dei corsi dello studente oppure stampa il messaggio "Lo studente è già iscritto al corso {course}."
get_courses(): restituisce la lista dei corsi ai quali lo studente è iscritto.

Classe School:
Attributi:
students: dict[str, Student] - un dizionario per memorizzare gli studenti, in cui la chiave è una stringa ID mentre il valore è un oggetto di tipo Studente.
Metodi:
create_student(student_id: str): crea un nuovo studente con l'ID specificato e una lista di corsi vuota oppure stampa il messaggio "Lo studente con ID {student_id} esiste già."
enroll_student(student_id: str, course: str): se lo studente esiste viene iscritto al corso specificato,
altrimenti  stampa il messaggio "Studente non trovato."
get_student_courses(student_id: str): se lo studente esiste restituisce la lista dei corsi dello studente con l'ID specificato,
altrimenti ritorna il messaggio "Studente non trovato."
get_stundent_list(): Ritorna una lista di tutte le chiavi all'interno del dizionario students.
search_by_course(self, course: str): Trova e restituisce tutti gli ID degli studenti iscritti ad un determinato corso. 
Restituisce una lista di tutte le chiavi all'interno del dizionario students che hanno il corso specificato tra i valori oppure il messaggio di errore "Nessuno studente è iscritto al corso {course}." 
se non ci sono studenti che frequentano il corso specificato.
'''
if False:
    
    class Student:
        def __init__(self, student_id: str):
            self.student_id = student_id
            self.courses: list[str] = []

        def enroll(self, course: str):
            if course not in self.courses:
                self.courses.append(course)
            else:
                print( f"Lo studente è già iscritto al corso {course}.")
        
        def get_courses(self):
            return self.courses

    class School:
        def __init__(self):
            self.students:dict[str, Student] = {}

        def create_student(self, student_id: str):
            if student_id not in self.students.keys():
                student: Student = Student(student_id)
                self.students[student_id] = student
            else:
                print(f"Lo studente con ID {student_id} esiste già.")


        def  enroll_student(self, student_id: str, course: str):   
            if student_id in self.students.keys():
                self.students[student_id].enroll(course)
            else:
                print(f"Studente non trovato.")

        
        def get_student_courses(self, student_id: str):
            if student_id in self.students.keys():
                self.students[student_id].get_courses()
                return self.students[student_id].courses
            else:
                return f"Studente non trovato."


        def get_student_list(self):
            student_list = []
            for i in self.students.keys():
                student_list.append(i)
            return student_list


        def search_by_course(self, course: str):
            list_st = []
            for i in self.students.keys():
                if course in self.students[i].courses:
                    list_st.append(i)

            if len(list_st) != 0:
                return list_st
            else:
                return f"Nessuno studente è iscritto al corso {course}."
        


    # Creazione di una nuova scuola
    scuola = School()

    # Creazione di nuovi studenti
    scuola.create_student("1001")
    scuola.create_student("1002")
    scuola.create_student("1003")

    # Iscrizione degli studenti ai corsi
    scuola.enroll_student("1001", "Matematica")
    scuola.enroll_student("1002", "Fisica")
    scuola.enroll_student("1003", "Chimica")

    # Verifica dei corsi degli studenti        # result:
    print(scuola.get_student_courses("1001"))  # Output atteso: ['Matematica']
    print(scuola.get_student_courses("1002"))  # Output atteso: ['Fisica']
    print(scuola.get_student_courses("1003"))  # Output atteso: ['Chimica']


    # Creazione di una nuova scuola
    scuola = School()

    # Creazione di nuovi studenti
    scuola.create_student("1001")

    # Iscrizione degli studenti ai corsi
    scuola.enroll_student("1001", "Matematica")
    scuola.enroll_student("1001", "Matematica")

    # Tentativo di iscrizione di un corso per uno studente non esistente
    scuola.enroll_student("1004", "Fisica")

    # Verifica dei corsi degli studenti
    print(scuola.get_student_courses("1001"))
    print(scuola.get_student_courses("1004"))

    # result:
    # Lo studente è già iscritto al corso Matematica.
    # Studente non trovato.
    # ['Matematica']
    # Studente non trovato.

        







	











	

