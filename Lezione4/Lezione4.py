#Esercizio 1:

'''Write a function check_value(), which takes a number as an argument.
Using if / else, the function should print whether the number is bigger, smaller,
or equal to 5'''

def check_value(x: int):
    if x > 5:
        print(f"{x} è maggiore di 5")
    elif x == 5:
        print(f"{x} é uguale a 5")
    else:
        print(f"{x} è minore di 5")

x = 6
check_value(x)

#---------------------------------------#

#Esercizio 2:

'''Write a function check_length(), which takes a string as an argument.
Using if / else, check if the length of the string is bigger, smaller, or equal to 10
characters.'''

def check_legth(x: str):
    if len(x) > 10:
        print(f"la lunghezza della stringa è{len(x)} pertanto è più lunga di 10 caratteri")
    elif len(x)==10:
        print(f"la lunghezza della stringa è {len(x)} pertanto è uguale a 10 caratteri ")        
    else:
        print(f"la lunghezza della stringa è {len(x)} pertanto è minore di 10 caratteri")

x = input("inserisci una frase:  ")
check_legth(x)

#-------------------------------------#

#Esercizio 3:

'''Write a function print_numbers(), which takes a list of numbers as argument.
Using a for loop, print each number one by one.'''

def print_numbers(a: int):
    for numbers in a:
        print(numbers)

a: list = [4,6,7,8,9,3,5,2,0]
print_numbers(a)

#-----------------------------------#

#Esercizio 4:

'''Write a function check_each(), which takes a list of numbers as argument.
Using a for loop, iterate through the list.
For each number, print “bigger” if it’s bigger than 5, “smaller” if it’s smaller than 5,
and “equal” if it’s equal to 5.'''

def check_each(b: int):
    for numbers in b:
        if numbers < 5:
            print(f"{numbers} is smaller than 5")
        elif numbers == 5:
            print(f"{numbers} is equal than 5")
        else:
            print(f"{numbers} is bigger than 5")

d = [1,2,3,4,5,6,7,8,9,10]
check_each(d)

#------------------------------------#

#Esercizio 5:

'''Write a function add_one(). It takes an integer as argument. The function adds 1 to
the integer and returns it.
Write another function add_one_to_list(). It takes a list of integers as argument.
Define a variable new_list in this function.
Using a for loop, iterate through the argument list.
Using add_one(), fill new_list with integers from the argument list incremented
by 1.
Print new_list.'''

def add_one(t: int):
    t+=1
    print(t)

def add_one_to_list(i: int):
    new_list = []
    for num in i :
        print(add_one(num))
    new_list.append(num)


lista = [1,2,3,4,5,6,7,8,99]

print(add_one_to_list(lista))











