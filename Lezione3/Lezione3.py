# Giammarco Prudenzi                   30/04/2024

# ES. 4-1:
'''
Think of at least three kinds of your favorite pizza. Store these pizza names in a list, and then use a for loop to print the name of each pizza.
• Modify your for loop to print a sentence using the name of the pizza, instead of printing just the name of the pizza.
For each pizza, you should have one line of output containing a simple statement like I like pepperoni pizza.
• Add a line at the end of your program, outside the for loop, that states how much you like pizza. The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, such as I really love pizza!
'''
# Soluzione ES. 4-1:

favourite_pizza: list[str] = ["Diavola","Margherita","Quattro formaggi"]
for pizza in favourite_pizza:
    print(f"pizze preferite:\n{pizza}")
    print(f" mi piace molto la pizza {pizza}")
            
print("Adoro la pizza")

# ES. 4-2:
'''
Think of at least three different animals that have a common characteristic. 
Store the names of these animals in a list, and then use a for loop to print out the name of each animal.
• Modify your program to print a statement about each animal, such as A dog would make a great pet.
• Add a line at the end of your program, stating what these animals have in common.
You could print a sentence, such as Any of these animals would make a great pet!'''

# Soluzione ES. 4-2:

animals: list[str] = ["pipistrello","gatto","gufo"]
for animal in animals:
    print(animal+ ":")
    print(f"il {animal} è molto agile al buio")

print("\nognuno di questi animali saprebbe muoversi molto bene al buio")

# ES. 4-3:

'''Use a for loop to print the numbers from 1 to 20, inclusive.'''

# Soluzione ES. 4-3:

for numbers in range(0,21):
    print(numbers)

# ES. 4-4:
'''
Make a list of the numbers from one to one million, and then use a for loop to print the numbers.
(If the output is taking too long, stop it by pressing CTRL-C or by closing the output window.)
'''
# Soluzione ES. 4-4:
if False:
    for num in range(0,1000001):
        print(num)

# ES. 4-5:
'''
 Make a list of the numbers from one to one million, and then use min() and max() to make sure your list actually starts at one and ends at one million.
 Also, use the sum() function to see how quickly Python can add a million numbers.
'''
# Soluzione ES. 4-5:

number_range: int = range(0,1000001)
print(f"Max: {max(number_range)}\n min: {min(number_range)}")
print(sum(number_range))

# ES. 4-6:
'''
Use the third argument of the range() function to make a list of the odd numbers from 1 to 20.
Use a for loop to print each number.
'''
# Soluzione ES. 4-6:

for number in range(1,21,2):
    print(number)

# ES. 4-7:
'''
Make a list of the multiples of 3, from 3 to 30.
Use a for loop to print the numbers in your list.
'''
# Soluzione ES. 4-7:

multi: list = []
for i in range(3,31,3):
    multi.append(i)
    
print(multi)

# ES. 4-8:
'''
A number raised to the third power is called a cube.
For example, the cube of 2 is written as 2**3 in Python.
Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), and use a for loop to print out the value of each cube.
'''
# Soluzione ES. 4-8:

for n in range(1,11):
    print(n**3)
    
# ES. 4-9:
'''
Use a list comprehension to generate a list of the first 10 cubes.
'''
# Soluzione ES. 4-9:

cubes: list[int] = [n**3 for n in range(1,11)]
print(cubes)

# ES. 4-10:
'''
Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
• Print the message The first three items in the list are:.
Then use a slice to print the first three items from that program’s list.
• Print the message Three items from the middle of the list are:.
Then use a slice to print three items from the middle of the list.
• Print the message The last three items in the list are:. Then use a slice to print the last three items in the list.
'''
# Soluzione ES. 4-10:

cubes: list[int] = [n**3 for n in range(1,11)]
print(cubes)
print(cubes[:3])
print(cubes[4:7])
print(cubes[-3:])

# ES. 4-11:
'''
Start with your program from Exercise 4-1. Make a copy of the list of pizzas, and call it friend_pizzas.
Then, do the following:
• Add a new pizza to the original list.
• Add a different pizza to the list friend_pizzas.
• Prove that you have two separate lists.
Print the message My favorite pizzas are:, and then use a for loop to print the first list.
Print the message My friend’s favorite pizzas are:, and then use a for loop to print the second list.
Make sure each new pizza is stored in the appropriate list.
'''
# ES. 4-12:
'''
All versions of foods.py in this section have avoided using for loops when printing, to save space.
Choose a version of foods.py, and write two for loops to print each list of foods.
'''
# Soluzione ES. 4-11 & 4-12:

favourite_pizza: list = ["Diavola","Margherita","Quattro formaggi"]

Friend_pizzas: list = favourite_pizza.copy()

favourite_pizza.append("Capricciosa")
Friend_pizzas.append("Boscaiola")

print("\nMy favorite pizzas are:")
for pizze in favourite_pizza:
    print(pizze)

print("\nMy friend’s favorite pizzas are:") 
for p in Friend_pizzas:
    print(p)
    
# ES. 4-14:
'''
Look through the original PEP 8 style guide at https://python.org/dev/peps/pep-0008.
You won’t use much of it now, but it might be interesting to skim through it.
'''
# ES. 4-15:
'''
Choose three of the programs you’ve written in this chapter and modify each one to comply with PEP 8.
'''
# Soluzione ES. 4-14 & 4-15:

if False:
    # 1)
    multi = []
    for i in range(3, 31, 3):
        multi.append(i)

    print(multi)
    
    # 2)
    number_range = range(0, 1000001)
    print(f"Massimo: {max(number_range)}\nminimo: {min(number_range)}")
    print(sum(number_range))
    
    # 3)
    animals = ["pipistrello", "gatto", "gufo"]
    for animal in animals:
        print(animal + ":")
        print(f"Il {animal} è molto agile al buio.")

# ES. 5-1:
'''
Write a series of conditional tests. Print a statement
describing each test and your prediction for the results of each test.
Your code should look something like this:
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
• Look closely at your results, and make sure you understand why each line
evaluates to True or False.
• Create at least 10 tests. Have at least 5 tests evaluate to True and another
5 tests evaluate to False.
'''
# Soluzione ES. 5-1:

bird = "eagle"

print("Is bird == 'eagle' ? I predict True.")
print(bird == "eagle")
print("\nIs bird == 'horse'? I predict False.")
print(bird == "horse")
print("\nIs bird != 'horse'? I predict True ")
print(bird != "horse")
print("\nIs bird != 'eagle'? I predict False ")
print(bird != "eagle")
print("\nIs bird == 'eagle'+'horse'? I predict False ")
print(bird == "eagle"+"horse")
print("\nIs 'horse' == 'eagle'? I predict False ")
print("horse" == "eagle")
print("\nIs Len(horse) < len('eagle')? I predict False ")
print(len("horse") < len("eagle"))
print("\nIs Len(horse) <= len('eagle')? I predict True ")
print(len("horse") <= len("eagle"))
print("\nIs 'horse'[4] == 'eagle'[4]? I predict True ")
print("horse"[4] == "eagle"[4])
print("\nIs bird == len('horse')? I predict True ")
print(bird != len('horse'))

# Per L'esercizio 5-2 ho creato un file conditional_tests.py sulla cartella Lezione3

# ES. 5-3, 5-4, 5-5:
'''
Imagine an alien was just shot down in a game. Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
• Write an if statement to test whether the alien’s color is green. If it is, print a message that the player just earned 5 points.
• Write one version of this program that passes the if test and another that fails.
(The version that fails will have no output.)

Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.
• If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.
• If the alien’s color isn’t green, print a statement that the player just earned 10 points.
• Write one version of this program that runs the if block and another that runs the else block.

into an if-elif-else chain.
• If the alien is green, print a message that the player earned 5 points.
• If the alien is yellow, print a message that the player earned 10 points.
• If the alien is red, print a message that the player earned 15 points.
• Write three versions of this program, making sure each message is printed for the appropriate color alien.
'''
# Soluzione ES. 5-3, 5-4, 5-5:

alien_color: str = "green"
if alien_color == "green":
    print("good job, you just earned 5 points ")
else:
    pass
    
if alien_color != "green":
    print("good job, you just earned 5 points")
else:
    pass

alien2_color: str = "red"

if alien_color == "green":
    print(f"good job you killed {alien_color} alien. You just earned 5 points")
elif alien_color == "red":
    print(f"good job you killed {alien2_color} alien. You just earned 15 points")
else:
    print("good job you killed yellow alien. You just earned 10 points")
    
if alien2_color == "green":
    print(f"good job you killed {alien_color} alien. You just earned 5 points")
elif alien2_color == "red":
    print(f"good job you killed {alien2_color} alien. You just earned 15 points")
else:
    print("good job you killed yellow alien. You just earned 10 points")
    
if alien2_color != "red":
    print(f"good job you killed {alien_color} alien. You just earned 5 points")
elif alien_color == "red":
    print(f"good job you killed {alien2_color} alien. You just earned 15 points")
else:
    print("good job you killed yellow alien. You just earned 10 points")
    
# ES. 5-6:
'''
Write an if-elif-else chain that determines a person’s stage of life. Set a value for the variable age, and then:
• If the person is less than 2 years old, print a message that the person is a baby.
• If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
• If the person is at least 4 years old but less than 13, print a message that the person is a kid.
• If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
• If the person is at least 20 years old but less than 65, print a message that the person is an adult.
• If the person is age 65 or older, print a message that the person is an elder.
'''
# Soluzione ES. 5-6:
if False:
    age: int = int(input("enter an age: "))

    if age < 2:
        print("that person is a baby")
    elif 4 < age < 13:
        print("that person is a toddler")
    elif 13 < age < 20:
        print("that person is a teenager")
    elif 20 < age < 65:
        print("that person is an adult")
    elif age >= 65:
        print("that person is an elder")
    
# ES. 5-7:
'''
Make a list of your favorite fruits, and then write a series of independent if statements that check for certain fruits in your list.
• Make a list of your three favorite fruits and call it favorite_fruits.
• Write five if statements.
Each should check whether a certain kind of fruit is in your list. If the fruit is in your list, the if block should print a statement, such as You really like Apples!
'''
# Soluzione ES. 5-7:

favourite_fruits: list[str] = ["apple","banana","watermelon"]
if "apple" in favourite_fruits:
    print(f"you really like {favourite_fruits[0]} ")
if "banana"in favourite_fruits[2]:
    print("you hate banana")
if favourite_fruits[2] is "watermelon":
    print("you really like watermelon") 
if "banana" and "watermelon" in favourite_fruits:
    print(f"you really like {favourite_fruits[1]} and {favourite_fruits[2]} ")
if "apple" or "banana"in favourite_fruits:
    print("I like classic fruit")
    
# ES. 5-8 & 5-9:
'''
Make a list of five or more usernames, including the name 'admin'. Imagine you are writing code that will print a greeting to each user after they log in to a website.
Loop through the list, and print a greeting to each user.
• If the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report?
• Otherwise, print a generic greeting, such as Hello Jaden, thank you for logging in again.

Add an if test to hello_admin.py to make sure the list of users is not empty.
• If the list is empty, print the message We need to find some users!
• Remove all of the usernames from your list, and make sure the correct message is printed.
'''
# Soluzione ES. 5-8 & 5-9:

usernames: list[str] = ["Max","Alessio","admin","Marco","Carlo"]
for user in usernames:
    if user == "admin":
        print("Hello admin, would you like to see a status report ?")
        continue
    else:
        print(f"Hello {user} ,thank you for logging in again.")

usernames.clear()
if user not in usernames:
    print("We need to find some users!")

# ES. 5-10:
'''
Do the following to create a program that simulates how websites ensure that everyone has a unique username.
• Make a list of five or more usernames called current_users.
• Make another list of five usernames called new_users. Make sure one or two of the new usernames are also in the current_users list.
• Loop through the new_users list to see if each new username has already been used.
If it has, print a message that the person will need to enter a new username.
If a username has not been used, print a message saying that the username is available.
• Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should not be accepted.
(To do this, you’ll need to make a copy of current_users containing the lowercase versions of all existing users.)
'''
# Soluzione ES. 5-10:

current_users: list[str] = ["Marc","Gimmi","Silvio","Kevin","Sandro","Rita"]

current_users_lower = [user.lower() for user in current_users]

new_users: list[str] = ["Biggio","Pioli","GiMMi","SaNDro","Jessica","Leao"]

for users in new_users:
    if users.lower() in current_users_lower:
        print("sorry, this username already exists. Will need to enter a new username.")
    else:
        print(f"{users} ? yes, this username is available")
        
# ES. 5-11:
'''
Ordinal numbers indicate their position in a list, such as 1st or 2nd.
Most ordinal numbers end in th, except 1, 2, and 3.
• Store the numbers 1 through 9 in a list.
• Loop through the list.
• Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number.
Your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th", and each result should be on a separate line.
'''








        
        




    

    
    
    
    
    
    

















    
    
    
    
    
    



    




    


    


    
   

    







