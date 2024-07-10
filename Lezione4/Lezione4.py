# Giammarco Prudenzi                  30/04/2024

# ES. 8-1
'''
Write a function called display_message() that prints one sentence telling everyone what you are learning about in this chapter.
Call the function, and make sure the message displays correctly.
'''
# Soluzione ES. 8-1:

if False:
    def display_message() -> str:
        print("in this chapter we are learning how to use functions, how to use them and their structure.")
    
    display_message()

# ES. 8-2:
'''
Write a function called favorite_book() that accepts one parameter, title. The function should print a message, such as "One of my favorite books is Alice in Wonderland".
Call the function, making sure to include a book title as an argument in the function call.
'''
# Soluzione ES. 8-2:

if False:
    def favourite_book(title: str)-> str:
        print("One of my favorite books is The Lord of the Rings")

    favourite_book("Lord of the Rings")

# ES. 8-3:
'''
Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
The function should print a sentence summarizing the size of the shirt and the message printed on it.
Call the function once using positional arguments to make a shirt.
Call the function a second time using keyword arguments.
'''
# Soluzione ES. 8-3:

if False:
    def make_shirt(size: str, text: str)-> str:
        print(f"size t-shirt: {size}")
        print(f"text of a message that should be printed on the shirt:\n{text}")

    make_shirt("L","Hello world")
    make_shirt(size= "M", text= "Vida Loca")

# ES. 8-4:
'''
Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. 
Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.
'''
# Soluzione ES. 8-4:

if False:  
    def make_shirt(size: str = "L", text: str = "I love python")-> str:
        print(f"size t-shirt: {size}")
        print(f"text of a message that should be printed on the shirt:\n{text}")

    make_shirt()
    make_shirt("M")
    make_shirt(text="The day after tomorrow")

# ES. 8-5:
'''
Write a function called describe_city() that accepts the name of a city and its country.
The function should print a simple sentence, such as Reykjavik is in Iceland.
Give the parameter for the country a default value. 
Call your function for three different cities, at least one of which is not in the default country.
'''
# Soluzione ES. 8-5:

if False:
    def describe_city(city: str, country: str = "Italy")-> str:
        print(f"{city} is in {country}")

    describe_city("Firenze")
    describe_city("Rome")
    describe_city("Tokyo","japan")

# ES. 8-6:
'''
Write a function called city_country() that takes in the name of a city and its country.
The function should return a string formatted like this: "Santiago, Chile".
Call your function with at least three city-country pairs, and print the values that are returned.
'''
# Soluzione ES. 8-6:

if False:
    def city_country(city: str, country: str)-> str:
        print(f"{city},{country}")

    city_country("Paris","France")
    city_country("Madrid","Spain")
    city_country(city="Oslo",country="Norway")

# ES. 8-7 & 8-8:
'''
Write a function called make_album() that builds a dictionary describing a music album.
The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information.
Use the function to make three dictionaries representing different albums.
Print each return value to show that the  dictionaries are storing the album information correctly.
Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album. If the calling line includes a value for the number of songs, add that value to the album’s dictionary.
Make at least one new function call that includes the number of songs on an album.

Start with your program from Exercise 8-7.
Write a while loop that allows users to enter an album’s artist and title.
Once you have that information, call make_album() with the user’s input and print the dictionary that’s created.
Be sure to include a quit value in the while loop.
'''
# Soluzione ES. 8-7 & 8-8:

if False:
    def make_album(Band: str, album: str, number_songs_album: int = None )-> dict:
        info = {"name":Band, "album":album}
        if number_songs_album:
            info["number_songs_album"]= number_songs_album
        return info

    print(make_album("Metallica","Master of Puppets"))
    print(make_album("Iron Maiden","Fear of the Dark"))
    print(make_album("Linkin Park","Meteora"))
    print(make_album("Pink Floyd","The Wall",26))

    while True:
        print("enter 'q' at any time to quit")
    
        band = input("enter the name of the Band: ")
        if band == "q":
            break
    
        albums = input("enter the name of the album: ")
        if albums == "q":
            break
    
    print(make_album(band,albums))

# ES. 8-9 & 8-10 & 8-11:
'''
Make a list containing a series of short text messages.
Pass the list to a function called show_messages(), which prints each text message.

Start with a copy of your program from Exercise 8-9. Write a function called send_messages() that prints each text message and moves each message to a new list called sent_messages as it’s printed.
After calling the function, print both of your lists to make sure the messages were moved correctly.

start with your work from Exercise 8-10. Call the function send_messages() with a copy of the list of messages.
After calling the function, print both of your lists to show that the original list has retained its messages.
'''

# Soluzione ES. 8-9 & 8-10 & 8-11:

if False:
    short_text: list[str] = ["Ciao,come stai?","Vuoi uscire dal programma","lo sapevo","hai ragione"]
    sent_message = []
    new_short_text = short_text.copy()

    def show_messages(text: str)-> str:
        for m in text:
            print(m)

    show_messages(short_text)

    def send_messages(text: list[str] ,sent_messages: list[str])-> list[str]:
        while text:
            mex = text.pop()
            print(mex)
            sent_messages.append(mex)

    send_messages(short_text[:], sent_message)
    print(f"original list: {short_text}")
    print(f"new list: {sent_message}")
    send_messages(short_text[:], new_short_text)
    print(f"original list: {short_text}")
    print(f"copy of original list: {new_short_text}")
    
    
# ES. 8-12:
'''
Write a function that accepts a list of items a person wants on a sandwich.
The function should have one parameter that collects as many items as the function call provides,
and it should print a summary of the sandwich that’s being ordered.
Call the function three times, using a different number of arguments each time.
'''
# Soluzione ES. 8-12:

if False:
    def sandwich(*items: list[str])-> str:
    
        print("\nItems in the sandwich:")
        for item in items:
            print(f"- {item}")

    sandwich("salad","pepperoni","tabasco","cheese")
    sandwich("maionese","ham")
    sandwich("cucumbers","mozzarella","tomatoes")

# ES. 8-13:
'''
Build a profile of yourself by calling build_profile(), using your first and last names and three other key-value pairs that describe you.
All the values must be passed to the function as parameters.
The function then must return a string such as "Eric Crow, age 45, hair brown, weight 67"
'''
# Soluzione ES. 8-13:

if False:
    def build_profile(first_name: str, last_name: str, age: int, weight: int, height: int):

        info = f"{first_name} {last_name}, age {age}, weight {weight}, height {height}"
        return info

    myprofile = build_profile("Giammarco","prudenzi", 27, 74, 180)
    print(myprofile)

# ES. 8-14:
'''
Write a function that stores information about a car in a dictionary. 
The function should always receive a manufacturer and a model name.
It should then accept an arbitrary number of keyword arguments.
Call the function with the required information and two other name-value pairs, such as a color or an optional feature.
Your function should work for a call like this one:
car = make_car('subaru', 'outback', color='blue', tow_package=True) Print the dictionary that’s returned to make sure all the information was stored correctly. 
'''
# Soluzione ES. 8-14:

if False:
    def info_car(manufacture: str, model_name: str, **build):
    
        build["manufacture"] = manufacture
        build["model_name"] = model_name
        return build

    build_car = info_car("Bmw","Z4", color= "black", tow_package=True) 
    print(build_car)

# ES. 8-15 & 8-16:
'''
Put the functions for the example printing_models.py in a separate file called printing_functions.py.
Write an import statement at the top of printing_models.py, and modify the file to use the imported functions.

Using a program you wrote that has one function in it, store that function in a separate file. 
Import the function into your main program file, and call the function using each of these approaches:
import module_name
from module_name import function_name
from module_name import function_name as fn
import module_name as mn
from module_name import *
'''
# Soluzione ES. 8-15 & 8-16:

if False:
    import printing_functions
    from printing_functions import info_car
    from printing_functions import info_car as mn
    from printing_functions import*

    printing_functions.info_car("Toyota","Yaris",color = "Blue", tow_package= True)

# ES. 8-17:
'''
Choose any three programs you wrote for this chapter.
make sure they follow the styling guidelines described in this section.
'''
# Soluzione ES. 8-17:

if False:
    # 1)
    def sandwich(*items: list[str]) -> str:
        """
        Stampa gli ingredienti di un panino.

        :param items: Una lista di ingredienti.
        :return: Una stringa che conferma gli ingredienti del panino.
        """

        print("\nIngredienti del panino:")
        for item in items:
            print(f"- {item}")
            
            return "Panino preparato con successo!"

    
    # 2)
    def info_car(manufacture: str, model_name: str, **build) -> dict:
     """
     Restituisce un dizionario che contiene i dettagli dell'auto.

        :param manufacture: Il produttore dell'auto.
        :param model_name: Il modello dell'auto.
        :param build: Altri dettagli dell'auto.
        :return: Un dizionario che contiene i dettagli dell'auto.
        """

     build["manufacture"] = manufacture
     build["model_name"] = model_name

     return build


    build_car = info_car("Bmw", "Z4", color="black", tow_package=True)
    print(build_car)
    
    # 3)
    def city_country(city: str, country: str) -> str:
        """
        Restituisce una stringa che rappresenta la città e il paese.

        :param city: Il nome della città da includere nella stringa.
        :param country: Il nome del paese da includere nella stringa.
        :return: Una stringa che contiene il nome della città e il nome del paese.
        """

        return f"{city}, {country}"


    print(city_country("Paris", "France"))
    print(city_country("Madrid", "Spain"))
    print(city_country(city="Oslo", country="Norway"))
    

# ESERCIZI LEZIONE4 (OPZIONALI):

# ES. 1:
'''
 Create a function that takes a student's name and their scores in different subjects as input.
The function calculates the average score and prints the student's name, average, and a message indicating whether the student passed the exam (average >= 60) or failed.
Create a for loop to iterate over a list of students and scores, calling the function for each student.
''' 
# Soluzione ES. 1:

if False:

    def students_score(name: str, score: list[float]):
        counter = 0
        for s in score:
            counter += s     
        if counter / len(score) >= 60:
            return f" studente: \n{name}\nmedia:\n {round(counter/len(score),2)}\nesito: \nprommosso\n"
        else:
            return f"studente: \n{name}\nmedia:\n {round(counter/len(score),2)}\nesito: \nbocciato\n"
                      
    Luca = students_score(name="Luca",score=[50,50,60,70])
    Alice = students_score("Alice",[90,80,85,80])
    Sandro = students_score("Sandro",[70,75,72,68])
    
    list_student = [Luca,Alice,Sandro]
    
    for student in list_student:
        print(student)
        
# ES. 2:
'''
Create a function that generates a random number within a range specified by the user.
Prompt the user to guess the number within a specified maximum number of attempts.
Provide feedback to the user after each guess, indicating whether their guess is too high, too low, or correct.
Terminate the loop when the user guesses the number correctly or reaches the maximum number of attempts.
'''
# Svolgimento ES. 2:

if False:
    from random import*

    def casual_number():
        tentativi = 0
        num = int(input("inserisci un numero: "))
        num1 = randint(0,num)
        num_num = int(input("inserisci un numero che credi sia giusto: "))
        while num1 != num_num:
            tentativi += 1
            if num1 == num_num:
                return f"Bravo hai indovinato, il numero giusto era {num}"
            elif num1 > num_num:
                return f"la tua ipotesi è piu alta del numero scelto, riprova!!\n numero tentativi: {tentativi}"
            else:
                return f"la tua ipotesi è più bassa del numero scelto, riprova!!\n numero tentativi: {tentativi}"
                    
    
    print(casual_number())


# ES. 3 E-commerce Shopping Cart:
'''
Create a function that defines a product with a name, price, and quantity.
Create a function that manages the shopping cart, allowing the user to add, remove, and view products in the cart.
The function should calculate the cart total and apply any discounts or taxes.
Implement a for loop to iterate over the items in the cart and print detailed information about each product and the total.
'''
# Svolgimento ES. 3:

if False:

    def product(name: str, price: float, quantity: int):
        product = {}
        product["name"] = name
        product["price"] = price
        product["quantity"] = quantity
        return product
    
    def add_product(shopping_cart: list, product: product):
        shopping_cart.append(product)
    
    def remove_product(shopping_cart: list, product: product):
        shopping_cart.remove(product)
    
    def total_price(shopping_cart: list[product]):

        tot = sum(p["price"] * p["quantity"] for p in shopping_cart)
        return f"Totale spesa: {tot} €"
                           
                            
        
    Mouse = product("Mouse", 20.50, 5)
    Cuffie = product("Cuffie", 90, 6)        
    MicroSD = product("MicroSD 64 GB", 17.99, 3)     

    shopping_cart = []

    add_product(shopping_cart,Mouse)
    add_product(shopping_cart,Cuffie)
    add_product(shopping_cart,MicroSD)
    remove_product(shopping_cart,Cuffie)

    print(shopping_cart)
    print(total_price(shopping_cart))


# ES. 4 Text Analysis:
'''
Create a function that reads a text file and counts the number of occurrences of each word.
The function should print a report showing the most frequent words and their number of occurrences.
You can use a for loop to iterate over the words in the text and a dictionary to store the occurrences.
Implement error handling to handle missing files or other input issues.
'''
# Svolgimento ES. 4:

if False:
    
    def occurrences_text(text: str):  # metodo per determinare quante parole vengono ripetute in un testo o file: 
        word_count = {}               
        word = text.lower().split()  
        for w in word:
            word_count[w] = word_count.get(w, 0) + 1  # metodo fondamentale (metodo .get())   
            for k,v in word_count.items():
                    print(f"word: {k} -> occurrences: {v}") # con print itera il dict con return no 

    text1 = '''e ci trovammo li, al cospetto di Borg il re serpente.
    Borg, è sempre stato un sovrano temuto in tutto il regno del serpente dorato ed ha sempre creduto 
    che un giorno il grande serpente della quarta era sarebbe tornato con un dono che avrebbe reso il regno 
    il più potente dei 5 regni sovrani comandati dai 5 ordini del serpente dorato e di ametista'''

    occurrences_text(text1) 
    

# ES. 5 Inventory Management System:  (con utilizzo delle classi)
'''
Create a function that defines an item with a code, name, quantity, and price.
Create a database or dictionary to store the items in inventory.
Implement functions to add, remove, search, and update items in the inventory.
Use for loops and conditional statements to manage the various inventory operations.
'''
# Svolgimento ES. 5:

if True:
    class Items:
        def __init__(self, code: str, name: str, quantity: int, price: float):
            self.code = code
            self.name = name
            self.quantity = quantity
            self.price = price
            
    class Database:
        def __init__(self):
            self.database = {}
        
        def add_items(self, items: Items):
            items[ items.name] = items
            self.database.append(items)
        
        def remove_items(self, items: Items):
            pass
        
        def search_items(self, items: Items):
            pass
            
        def update_items(self):
            pass

    database = Database()
    forbici = Items("2345", "forbici",5,10)
    forbici = Items("2697", "cuffie",10,30)
    forbici = Items("9786", "penna",30,2)
        

# ES.6 Password Generator:
'''
Create a function that generates a random password with a specified length and
desired character types (lowercase letters, uppercase letters, numbers, symbols).
Allow the user to specify the password length and desired character types.
Generate and return a random password that meets the user's criteria.
'''
# Svolgimento ES. 6:


# ES. 7 Roman Numeral Conversion:
'''
Create a function that converts a given integer to its Roman numeral representation.
Handle numbers from 1 to 3999.
Use a combination of string manipulation and conditional statements to build the Roman numeral.
'''
# Svolgimento ES. 7:


# ES. 8 ATM Machine Simulator:
'''
Create a function that simulates an ATM machine.
Initialize an account with a starting balance.
Allow the user to perform transactions such as deposit, withdraw, and check balance.
Validate transactions against the account balance and available funds.
Provide appropriate feedback to the user for each transaction.
'''
# Svolgimento ES. 8:


# ES. 9 Caesar Cipher Encryption/Decryption:
'''
Create functions for encrypting and decrypting a message using the Caesar cipher.
Allow the user to specify the shift value (number of positions to shift each letter).
Handle both encryption and decryption using the same function with appropriate adjustments.
Encrypt and decrypt the given message using the specified shift value.
'''
# Svolgimento ES. 9:


# ES. 10 Anagram Checker:
'''
Create a function that checks whether two given strings are anagrams of each other.
Convert both strings to lowercase and remove any non-alphabetic characters.
Sort the characters of each string and compare the sorted strings for equality.
Indicate whether the strings are anagrams or not.
'''
# Svolgimento ES. 10:


# ES. 11 Word Search Puzzle Solver:
'''
Create a function that solves a word search puzzle.
Provide a 2D grid representing the puzzle and a list of words to find.
Implement a backtracking algorithm to search for the words in the grid, marking visited cells to avoid repetition.
Output the locations of the found words within the grid.
'''
# Svolgimento ES. 11:


#ES. 12 Sieve of Eratosthenes Prime Number Generator:
'''
Create a function that generates a list of prime numbers up to a specified limit using the Sieve of Eratosthenes algorithm.
Initialize an array of all numbers up to the limit, marking each number as prime initially.
Iterate through the array, starting from 2, and mark every multiple of the current number as non-prime.
The remaining unmarked numbers are the prime numbers within the limit.
Return the list of prime numbers.
'''
# Svolgimento ES. 12:


# ES. 13 Fractal Tree Generator:
'''
Create a function that generates a fractal tree using recursion.
Specify the starting trunk length and branching angle.
Draw the trunk and then recursively call the function to draw two branches at the specified angle, each with a shorter length.
Repeat the branching process until a desired level of detail is reached.
'''
# Svolgimento ES. 13:


# ES. 14 Sudoku Solver:
'''
Create a function that solves a Sudoku puzzle using backtracking.
Provide a 9x9 grid representing the puzzle with some numbers filled in and others left blank.
Implement a backtracking algorithm to check for valid placements in empty cells, ensuring no row, column, or 3x3 subgrid contains duplicates.
Solve the puzzle by filling in the remaining empty cells with valid numbers.
'''
# Svolgimento ES. 14:

# ES. 15 Text Editor with Basic Functionality:
'''
Create a simple text editor that allows the user to open, edit, and save text files.
Implement basic functionality such as inserting, deleting, and copying text.
Provide undo/redo functionality to allow users to reverse actions.
Save the edited text to a file when the user chooses to save.
'''
# Svolgimento ES. 15:
            
            
            
            
            




    
        


    
    
    









    



    
    
    












