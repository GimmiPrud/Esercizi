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

# ES. 5-3:
'''
Imagine an alien was just shot down in a game. Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
• Write an if statement to test whether the alien’s color is green. If it is, print a message that the player just earned 5 points.
• Write one version of this program that passes the if test and another that fails.
(The version that fails will have no output.)
'''
# Soluzione ES. 5-3:














    
    
    
    
    
    



    




    


    


    
   

    







