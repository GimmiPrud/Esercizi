# Giammarco Prudenzi                  08/05/2024

# Esercizi Lezione6:

# ES. 9-1 & 9-2:
'''
 Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type.
Make a method called describe_restaurant() that prints these two pieces of information,
and a method called open_restaurant() that prints a message indicating that the restaurant is open.
Make an instance called restaurant from your class.
Print the two attributes individually, and then call both methods.
Create three different instances from the class, and call describe_restaurant() for each instance.
'''     
# Svolgimento ES. 9-1 & 9-2:

if False:

    class Restaurant:
        def __init__(self, restaurant_name: str, cuisine_type: str):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            return f"name restaurant = {self.restaurant_name}\ncuisine type = {self.cuisine_type}"


        def open_restaurant(self):
            return f"today {self.restaurant_name} is open"
        
    restaurant = Restaurant("Retrogusto","Italian")
    print(restaurant.describe_restaurant())
    print(restaurant.open_restaurant())
    restaurant1 = Restaurant("Osaka","Japanese")
    restaurant2 = Restaurant("Madeira","Brazilian")
    restaurant3 = Restaurant("La Baracca","Italian")
    print(restaurant1.describe_restaurant())
    print(restaurant2.describe_restaurant())
    print(restaurant3.describe_restaurant())

# ES. 9-3 & 9-5:
'''
Make a class called User. 
Create two attributes called first_name and last_name,
and then create several other attributes that are typically stored in a user profile.
Make a method called describe_user() that prints a summary of the user’s information.
Make another method called greet_user() that prints a personalized greeting to the user.
Create several instances representing different users, and call both methods for each user.

Add an attribute called login_attempts to your User class from Exercise 9-3.
Write a method called increment_login_attempts() that increments the value of login_attempts by 1.
Write another method called reset_login_attempts() that resets the value of login_attempts to 0. 
Make an instance of the User class and call increment_login_attempts() several times.
Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts().
Print login_attempts again to make sure it was reset to 0.
'''
# Svolgimento ES. 9-3 & 9-5:

if True:
    class User:
        def __init__(self, first_name: str, last_name: str, login_attempts: int = 0):
            self.first_name = first_name
            self.last_name = last_name
            self.age = None
            self.active = None
            self.login_attempts = login_attempts

        def describe_user(self, newage: int, newactive: bool = True):
            self.age = newage
            self.active = newactive
            return f"first name:\n- {self.first_name}\nlast name:\n- {self.last_name}\nage:\n- {self.age}\n active:\n- {self.active}\n login attempts:\n- {self.login_attempts}"
        
        def increment_login_attempts(self):
            while self.login_attempts:
                self.login_attempts += 1

        def reset_login_attempts(self):
            if self.login_attempts > 0:
                reset_login = self.login_attempts - range(self.login_attempts)

            return reset_login

        def greet_user(self):
            return f" Hello { self.first_name}, welcome!!"
        
    Giacomo = User("Giacomo","Panella")
    print(Giacomo.describe_user(33, False))
    print(Giacomo.greet_user())
    print(Giacomo.age)
    print(Giacomo.active)
    Alessio = User("Alessio","Perazzino")
    print(Alessio.describe_user(26,True))
    print(Alessio.greet_user())
    Mattia = User("Mattia","Campanelli")
    print(Mattia.describe_user(26,False))
    print(Mattia.increment_login_attempts())

# ES. 9-4:
'''
Start with your program from Exercise 9-1.
Add an attribute called number_served with a default value of 0.
Create an instance called restaurant from this class.
Print the number of customers the restaurant has served, and then change this value and print it again.
Add a method called set_number_served() that lets you set the number of customers that have been served. 
Call this method with a new number and print the value again. Add a method called increment_number_served() that lets you increment the number of customers who’ve been served.
Call this method with any number you like that could represent how many customers were served in, say, a day of business. 
'''
# Svolgimento ES. 9-4:

if False:
    class Restaurant:
        def __init__(self, restaurant_name: str, cuisine_type: str, number_served: int = 0):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.number_served = number_served

        def describe_restaurant(self):
            return f"name restaurant = {self.restaurant_name}\ncuisine type = {self.cuisine_type}"
        
        def set_number_served(self,new_number_served: int):
            self.number_served = new_number_served
            return f" Customers served = {self.number_served}"
        
        def increment_number_served(self, increment: int):
            increment = self.number_served + increment
            return f" number served today  = {increment}"

        def open_restaurant(self):
            return f"today {self.restaurant_name} is open"
        
        
    restaurant = Restaurant("Da Ciccio","Italian",10)
    print(restaurant.describe_restaurant())
    print(restaurant.number_served)
    print(restaurant.set_number_served(5))
    print(restaurant.increment_number_served(40))













