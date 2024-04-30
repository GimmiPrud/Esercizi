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

def make_album(Band: str, album: str, number_songs_album: int = None )-> dict:
    info = {"name":Band, "album":album}
    if number_songs_album:
        info["number_songs_album"]= number_songs_album
    return info

print(make_album("Metallica","Master of Puppets"))
print(make_album("Iron Maiden","Fear of the Dark"))
print(make_album("Linkin Park","Meteora"))
print(make_album("Pink Floyd","The Wall"))

while True:
    print("enter 'q' at any time to quit")
    
    band = input("enter the name of the Band: ")
    if band == "q":
        break
    
    albums = input("enter the name of the album: ")
    if albums == "q":
        break
    
print(make_album(band,albums))

# ES. 8-9:
'''
Make a list containing a series of short text messages.
Pass the list to a function called show_messages(), which prints each text message.
'''
# Soluzione ES. 8-9






    



    
    
    












