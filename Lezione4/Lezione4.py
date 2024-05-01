# Giammarco Prudenzi                  30/04/2024

# ES. 8-1
'''
Write a function called display_message() that prints one sentence telling everyone what you are learning about in this chapter.
Call the function, and make sure the message displays correctly.
'''
# Soluzione ES. 8-1:

def display_message() -> str:
    print("in this chapter we are learning how to use functions, how to use them and their structure.")

display_message()

# ES. 8-2:
'''
Write a function called favorite_book() that accepts one parameter, title. The function should print a message, such as "One of my favorite books is Alice in Wonderland".
Call the function, making sure to include a book title as an argument in the function call.
'''
# Soluzione ES. 8-2:

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

short_text: list[str] = ["Ciao,come stai?","Vuoi uscire dal programma","lo sapevo","hai ragione"]

def show_messages(text: str)-> str:
    for t in text:
        print(t)
    return text

show_messages(short_text)

sent_messages: list[str] = []

def send_messages(short_text: list[str],sent_messages: list[str])->list[str]:
    pass


# ES. 8-12:
'''
Write a function that accepts a list of items a person wants on a sandwich.
The function should have one parameter that collects as many items as the function call provides,
and it should print a summary of the sandwich that’s being ordered.
Call the function three times, using a different number of arguments each time.
'''
# Soluzione ES. 8-12:

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

# ES. 8-15:
'''
Put the functions for the example printing_models.py in a separate file called printing_functions.py.
Write an import statement at the top of printing_models.py, and modify the file to use the imported functions.
'''
# Soluzione ES. 8-15:
if False:
    import printing_functions

    printing_functions.info_car("Toyota","Yaris",color = "Blue", tow_package= True)

    
    
    









    



    
    
    












