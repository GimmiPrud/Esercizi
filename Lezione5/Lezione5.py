# Giammarco Prudenzi                   02/05/2024

# Esercizi Lezione5:

# ES. 1:
'''
Scrivi una funzione che somma tutti i numeri interi di una lista che sono maggiori
di un dato valore intero definito threshold.
'''
# Svolgimento ES. 1:

if False:
    def sum_above_threshold(numbers: list[int], threshold: int) -> int:
        sum = 0
        for number in numbers:
            if number > threshold:
                sum += number
        return sum

    print(sum_above_threshold([15, 5, 25], 20))

# ES. 2:
'''
Scrivi una funzione che riceve un numero e stampa un conto alla rovescia da quel numero a zero.
''' 
# Svolgimento ES. 2:

if False:
    def countdown(n: int) -> int:
        for i in range(n,-1,-1):
            print(i)

    countdown(5)

# ES. 3:
'''
Scrivi una funzione che accetti tre parametri: username, password e status di attivazione dell'account (attivo/non attivo).
L'accesso è consentito solo se il nome utente è "admin", la password corrisponde a "12345" e l'account è attivo.
La funzione ritorna "Accesso consentito" oppure "Accesso negato".
'''
# Svolgimento ES. 3:

if False:
    def check_access(username: str, password: str, is_active: bool) -> str:
        if username == "admin" and password == "12345" and is_active == True:
            return "Accesso consentito"
        else:
            return "Accesso negato"
    
    print(check_access("admin", "12345", True))
    print(check_access("admin", "54321", True))

# ES. 4:
'''
Scrivi una funzione che, data una lista,
ritorni un dictionary che mappa ogni elemento alla sua frequenza nella lista.
'''
# Svolgimento ES. 4:

if False:
    def frequency_dict(elements: list) -> dict:
        elements_dict = {}
        for e in elements:
            elements_dict[e] = elements_dict.get(e,0)+1
        return elements_dict
    
    print(frequency_dict(['mela', 'banana', 'mela']))
    
# ES. 5:
'''
Scrivi una funzione che converte una temperatura da gradi Celsius a Fahrenheit e viceversa a seconda del parametro to_fahrenheit. 
Utilizza il concetto di parametri opzionali per il parametro to_fahrenheit.
'''
# Svolgimento ES. 5:

if False:
    def convert_temperature(to_fahrenheit: float, Celsius: bool = False) -> float:
        if Celsius == False:
            print ((to_fahrenheit * 1.8) + 32 , "°F") 
        
        if Celsius == True:
            print((to_fahrenheit - 32) / 1.8, "°C")
        
    convert_temperature(32, True)
    convert_temperature(0,False)
    convert_temperature(to_fahrenheit=50, Celsius= False)
    convert_temperature( 10, 0)
            

# ES. 6:
'''
Scrivi una funzione che verifica se una combinazione di condizioni (A, B, e C) è soddisfatta per procedere con un'operazione.
L'operazione può procedere solo se la condizione A è vera o se entrambe le condizioni B e C sono vere. 
La funzione deve ritornare "Operazione permessa" oppure "Operazione negata" a seconda delle condizioni che sono soddisfatte.
'''
# Svolgimento ES. 6:

if False:
    def check_combination(conditionA: bool, conditionB: bool, conditionC: bool) -> str:
        if conditionA == True:
            return "Operazione permessa"
        elif conditionB and conditionC == True:
            return "Operazione permessa"
        else:
            return "Operazione negata"
    
    print(check_combination(True, False, True))
    print(check_combination(False, True, False))
    
# ES. 7:
'''
Scrivi una funzione che verifica se in una stringa le parentesi '(' e ')' sono bilanciate,
cioè per ogni parentesi che apre c'è la corrispondente parentesi che chiude.
'''
# Svolgimento ES. 7:

if False:
    def check_parentheses(expression: str) -> bool:
        return expression.count('(') == expression.count(')') and expression[0]=='('and expression[-1]==')'

# ES. 8:
'''
Scrivi una funzione che conta e ritorna quante volte un elemento appare isolato in una lista di numeri interi.
Un elemento è considerato isolato se non è affiancato sia a destra che a sinistra da elementi uguali.
'''
# Svolgimento ES. 8:

if False:
    def count_isolated(num_list: list[int]) -> int:                         
        count = 0
        for n in range(len(num_list)):
             if num_list[n] != num_list[n-1] and (n == len(num_list)-1 or num_list[n] != num_list[n+1]):
                count += 1
        return count
                     
    print(count_isolated([1, 2, 2, 3, 3, 3, 4]))
    print(count_isolated([1, 1, 2, 2, 3, 4, 4]))
    print(count_isolated([1, 2, 3, 4, 5]))
    print(count_isolated([1,1,1,1,1,1]))
    print(count_isolated([]))
        

# ES. 9:
'''
Scrivi una funzione che, dato un insieme e una lista di numeri interi da rimuovere, 
ritorni un nuovo insieme senza i numeri specificati nella lista.
'''
# Svolgimento ES. 9:

if False:
    def remove_elements(original_set: set[int], elements_to_remove: list[int]) -> set[int]:
        original_set.difference(elements_to_remove)
        dict_remove = original_set.difference_update(elements_to_remove)
        return original_set
    
    print(remove_elements({5, 6, 7}, [7, 8, 9]))
    
# ES. 10:
'''
Scrivi una funzione che unisce due dizionari.
Se una chiave è presente in entrambi, somma i loro valori.
'''
# Soluzione ES. 10:

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

    print(merge_dictionaries({'x': 5}, {'x': -5}))


# Esercizi opzionali:

# ES 1. Create a Playlist:
'''
Write a function called create_playlist() that accepts a playlist name and a variable number of song titles.
The function should return a dictionary with the playlist name and a set of songs.
Call the function with different numbers of songs to demonstrate flexibility.

Example: create_playlist("Road Trip", {"Song 1", "Song 2"})

Write a function called add_like() that accepts a dictionary, the name of a playlist, and a boolean value indicating whether it is liked (True or False). This function should return an updated dictionary.

Example: add_like(dictionary, “Road Trip”, liked=True)
'''
# Svolgimento ES. 1:
        


# 2. Book Collection:
'''
Write a function called add_book() that accepts an author's name and a variable number of book titles authored by them. 
This function should return a dictionary where the author's name is the key and the value is a list of their books.
Demonstrate this function by adding books for different authors.

Example: add_book("Mark Twain", ["The Adventures of Tom Sawyer", "Life on the Mississippi"])

Write a function called delete_book() that accepts a dictionary and the name of the author from whom to remove all details. This function should return an updated dictionary.

Example: delete_book(dictionary, “Mark Twain”)
'''
# Svolgimento ES. 2:


#ES 3. Personal Info:
'''
Write a build_profile() function that accepts the name , surname,  occupation, location, and age  of a person. Make occupation, location, and age optional parameters. Use this function to create profiles for different people, demonstrating how it handles these optional parameters.

Example: build_profile("John", "Doe", occupation="Developer", location="USA", age=30)
'''
# Svolgimento ES. 3:


#ES 4. Event Organizer:
'''
Write a function called plan_event() that accepts an event name, a list of participants, and an hour. The function should return a dictionary that includes the event name and a list of the participants. Call this function with varying numbers of participants to plan different events.

Example: plan_event("Code Workshop", ["Alice", "Bob", "Charlie"],”4pm”)

Write a function called modify_event() that accepts a dictionary, an event name, and new details to modify an already planned event.

Example: modify_event(dictionary, "Code Workshop", ["Alice", "Bob", "Charlie"], ”4pm”)
'''
# Svolgimento ES. 4:


# ES 5. Shopping List:
'''
Write a function called create_shopping_list() that accepts a store name and any number of items as arguments. It should return a dictionary with the store name and a set of items to buy there. Test the function with different stores and item lists.

Example: create_shopping_list("Grocery Store", {"Milk", "Eggs", "Bread"})

Write a function called print_shopping_list() that accepts a dictionary and a store name, then prints each item from that store's shopping list.

Example: print_shopping_list(dictionary, "Grocery Store")
'''
# Svolgimento ES. 5: