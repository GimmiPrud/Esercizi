# Giammarco Prudenzi                       18/04/2024

# ES. 2-3:
'''Use a variable to represent a person’s name, and print a message to that person.
Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?”'''

# Soluzione ES. 2-3:
name: str = "Alessio"

print(f"Ciao {name} would you like to learn some python today")

# ES. 2-4:
'''Use a variable to represent a person’s name. 
then print that person’s name in lowercase, uppercase, and title case.'''

# Soluzione ES. 2-4:
N: str = "Carletto"

print(N.upper(), N.title(), N.lower())
# oppure:
N: str = "Carletto"

N_lower = N.lower()
N_upper = N.upper()
N_title = N.title()

print(N_lower)
print(N_title)
print(N_upper)

# ES. 2-5:

'''Find a quote from a famous person you admire. Print the quote and the name of its author.
Your output should look something like the following, including the quotation marks:
Albert Einstein once said, “A person who never made a mistake never tried anything new.”'''

# Soluzione ES. 2-5:

name: str = "Thomas Edison"
cit: str = "\"Molti dei fallimenti della vita sono persone che non si sono rese conto di quanto fossero vicine al successo quando hanno rinunciato\""
print(f"{name} una volta disse:\n {cit}")

# ES. 2-8:

'''Python has a removesuffix() method that works exactly like removeprefix(). Assign the value 'python_notes.txt' to a variable called filename.
Then use the removesuffix() method to display the filename without the file extension, like some file browsers do'''

# Soluzione ES. 2-8:

File_name: str = 'python_notes.txt'

print(File_name.removesuffix('.txt'))

# ES. 3-1:

'''Store the names of a few of your friends in a list called names. 
Print each person’s name by accessing each element in the list, one at a time.'''

# Soluzione ES. 3-1:

names: list = ["Michele","Mattia","Giacomo","Andrea","Federico"]

name1 = names[0]
name2 = names[1]
name3 = names[2]
name4 = names[3]
name5 = names[4]  

print(name1, name2, name3, name4, name5 )

# ES. 3-2:

'''Start with the list you used in Exercise 3-1,
but instead of just printing each person’s name, 
print a message to them. 
The text of each message should be the same, 
but each message should be personalized with the person’s name.'''

# Soluzione ES. 3-2:

namess: list = ["Michele","Mattia","Giacomo","Andrea","Federico"]
for name in namess:
    print(f"{name} cosa fai oggi pomeriggio ?")

# Es. 3-3:

'''Think of your favorite mode of transportation,
such as a motorcycle or a car, and make a list that stores several examples.
Use your list to print a series of statements about these items, 
such as “I would like to own a Honda motorcycle.”'''

# Soluzione ES. 3-3:

machine: list = ["bmv","audi","toyota"]

print(f"mi piacerebbe sfrecciare con una {machine[0]} M5  ")

print(f"vorrei tanto possedere un {machine[1]} R1")

print(f"spero un giorno di correre con una {machine[2]} Supra")

# Soluzione ES. 3-4, 3-5, 3-6, 3,7:

people: list = ["Giulio Cesare","Napoleone","Dio"]

for p in people:
    
    print(f" Ciao {p} ci saresti questo fine settimana per una cena, ho già sentito gli altri")
    
print(f" Niente ,{people[2]} come sempre non c'è ")

people[2] = "Maradona"

for p in people:
    print(f" Ciao {p}, cena ore 20:00, puntuale")
    
print("aspettate ho trovato un tavolo più grande, quinidi penso che inviterò qualcun'altro")

people.insert(0,"Dante Alighieri")

people.insert(1,"Ozzy Osbourne")

people.append("Bruce Lee")

for p in people:
    print(f" Buonasera {p} alla fine siamo sei, ci vediamo direttamente a ristorante")

print(" Ragazzi mi dispiace ma non abbaimo piu il tavolo, c'è solo un tavolo per tre")

print(f"mi dispiace {people[0]} ma non posso più invitarti a cena")

people.pop(0)

print(f"mi dispiace {people[1]} ma non posso più invitarti a cena")

people.pop(1)

print(f"mi dispiace {people[2]} ma non posso più invitarti a cena")

people.pop(2)

print(f"mi dispiace {people[2]} ma non posso più invitarti a cena")

people.pop(1)

for p in people:
    print(f"{p} tu sei invitato a cena")

del(people[0:])

print(people)

# exit() per uscire dal programma.

# ES. 3-8:

'''Think of at least five places in the world you’d like to visit.
• Store the locations in a list. Make sure the list is not in alphabetical order.
• Print your list in its original order. Don’t worry about printing the list neatly; just print it as a raw Python list.
• Use sorted() to print your list in alphabetical order without modifying the actual list.
• Show that your list is still in its original order by printing it.
• Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.
• Show that your list is still in its original order by printing it again.
• Use reverse()  to change the order of your list. Print the list to show that its order has changed.
• Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
• Use sort() to change your list so it’s stored in alphabetical order.
Print the list to show that its order has been changed.
• Use sort() to change your list so it’s stored in reverse-alphabetical order.
Print the list to show that its order has changed.'''

# Soluzione ES. 3-8:

best_place: list = ["Hveravellir","Grotta Azzurra","Giappone","Taj Mahal","Caraibi"]

print(sorted(best_place))

print(best_place)

print(sorted(best_place, reverse= True))

print(best_place)

best_place.reverse()

print(best_place)

best_place.reverse()

print(best_place)

best_place.sort()

print(best_place)

best_place.sort(reverse= True)

print(best_place)

# ES. 3-9:
'''
Working with one of the programs from Exercises 3,
use len() to print a message indicating the number of people you’re inviting to dinner.'''

# Soluzione ES. 3-9:

# Continuo dell'esercizio 3-4/3-7:

people: list = ["Giulio Cesare","Napoleone","Dio"]

people_invite: int = len(people)

print(f"Il numero degli invitati è {people_invite}")

# ES. 3-10:
'''
Think of things you could store in a list. 
For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like.
Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.'''

# Soluzione ES. 3-10:

y = input("scrivi qualcosa: ")
x = []
x.append(y)
while y in x:
    z = input("scrivi qualcosa: ")
    x.append(z)
    if len(x) == 8:
        print(x)
        x.append("...")
        print(sorted(x))
        print(len(x))
        x.pop(2)
        x.insert(3,"barca")
        break

# ES. 6-1:

'''Use a dictionary to store information about a person you know.
Store their first name, last name, age, and the city in which they live. 
You should have keys such as first_name, last_name, age, and city.
Print each piece of information stored in your dictionary.'''

# Soluzione ES. 6-1:

user_information: dict = {"name":"Giacomo","last_name":"Panella","age":"32","city":"porano"}

for key,value in user_information.items():
    print(f"{key}:\n{value}")
    
# ES. 6-2:
'''
Use a dictionary to store people’s favorite numbers.
Think of five names, and use them as keys in your dictionary. 
Think of a favorite number for each person, and store each as a value in your dictionary.
Print each person’s name and their favorite number.
For even more fun, poll a few friends and get some actual data for your program.'''

# Soluzione ES. 6-2:

fav_numbers: dict = {"luca":25, "alessio":3, "matteo":31, "francesco":18, "damiano":7}

for name,number in fav_numbers.items():
    print(f"nome: {name}\n numero preferito: {number}")
    
# ES. 6-3:
'''
A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
• Think of five programming words you’ve learned about in the previous chapters.
Use these words as the keys in your glossary, and store their meanings as values.
• Print each word and its meaning as neatly formatted output. 
You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line.
Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.'''

# Soluzine ES. 6-3:

glossary: dict = {
"Kernel": "Nucleo centrale di un sistema operativo, che si occupa dell’interazione al livello più profondo tra il software e lo hardware su cui si trova installato",
"Booleano":"campo dell'analisi matematica nel quale si eseguono confronti. Operatori booleani possono essere ad esempio OR, AND, NOT, EQV, VERO (true), FALSO (false), ecc.",
"Debugger":"programma che agevola il compito di correzione degli errori che si commettono durante la creazione di un applicativo",
"Dir":"visualizza il contenuto di una directory",
"Funzione":"un insieme di istruzioni accumunate da un alias. Quests alias viene poi usato per richiamare l’insieme del codice, contenuto nella funzione stessa, senza doverlo scrivere nuovamente"
}

for k,v in glossary.items():
    print("Glossario informatico:\n",f"\n{k}:\n{v}")

# ES. 6-7:
'''
Start with the program you wrote for Exercise 6-1. 
Make two new dictionaries representing different people, and store all three dictionaries in a list called people.
Loop through your list of people.
As you loop through the list, print everything you know about each person.'''

# Soluzione ES. 6-7:

user1_information: dict = {"name":"Mattia","last_name":"campanelli","age":"26","city":"Castel Giorgio"}

user2_information: dict = {"name":"David","last_name":"Palmucci","age":"33","city":"Castel Giorgio"}

Person: list = [user_information, user1_information, user2_information]

for p in Person:
    print(p)
    
# ES. 6-8:
'''
Make several dictionaries, where each dictionary represents a different pet.
In each dictionary, include the kind of animal and the owner’s name. 
Store these dictionaries in a list called pets.
Next, loop through your list and as
you do, print everything you know about each pet. '''

# Soluzione ES. 6-8:

animal_1: dict = {"kind_of_animal":"Dog","owners_name":"Sergio"}

animal_2: dict = {"kind_of_animal":"Cat","owners_name":"Bruno"}

animal_3: dict = {"kind_of_animal":"Horse","owners_name":"Elena"}

pets: list = [animal_1, animal_2, animal_3]

for pet in pets:
    print(pet)
    
# ES. 6-9:
'''
Make a dictionary called favorite_places.
Think of three names to use as keys in the dictionary, and store one to three favorite places for each person.
To make this exercise a bit more interesting, ask some friends to name a few of their favorite places. 
Loop through the dictionary, and print each person’s name and their favorite places.'''

# Soluzione ES. 6-9:

Favorite_places: dict = {"Camilla":"New York","Alessandro":"Ibiza","Alma":"i Caraibi"}

for name,place in Favorite_places.items():
    print(f"Caio sono {name} e vorrei visitare {place}")
    
# ES. 6-10:
'''
Modify your program from Exercise 6-2 so each person can have more than one favorite number.
Then print each person’s name along with their favorite numbers.'''

# Soluzione ES. 6-10:

fav_numbers: dict = {
"luca":[25,56,6], 
"alessio":[34,78,45],
"matteo":[31,28,5],
"francesco":[18,48,2],
"damiano":[7,14,21]
}



    
    
    













    




    









































    

    





























  






