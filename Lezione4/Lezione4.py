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

# ES. 8-7:


    
    
    












