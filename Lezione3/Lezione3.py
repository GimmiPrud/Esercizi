# Giammarco Prudenzi                   30/04/2024

# ES. 4-1:
'''
Think of at least three kinds of your favorite pizza. Store these pizza names in a list, and then use a for loop to print the name of each pizza.
• Modify your for loop to print a sentence using the name of the pizza, instead of printing just the name of the pizza.
For each pizza, you should have one line of output containing a simple statement like I like pepperoni pizza.
• Add a line at the end of your program, outside the for loop, that states how much you like pizza. The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, such as I really love pizza!
'''
# Soluzione ES. 4-1:

favourite_pizza: list = ["Diavola","Margherita","Quattro formaggi"]
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

animals: list = ["pipistrello","gatto","gufo"]
for animal in animals:
    print(animal+ ":")
    print(f"il {animal} è molto agile al buio")

print("ognuno di questi animali saprebbe muoversi molto bene al buio")

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

for num in range(0,1000001):
   print(num)

# ES. 4-5:
'''
 Make a list of the numbers from one to one million, and then use min() and max() to make sure your list actually starts at one and ends at one million.
 Also, use the sum() function to see how quickly Python can add a million numbers.
'''
# Soluzione ES. 4-5:

number_range: int = range(0,1000001)
print(f"Massimo: {max(number_range)}\n minimo: {min(number_range)}")
print(sum(number_range))

# ES. 4-6:
'''
Use the third argument of the range() function to make a list of the odd numbers from 1 to 20.
Use a for loop to print each number.
'''
# Soluzione ES. 4-6:



    


    
   

    







