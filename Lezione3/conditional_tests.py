
# ES. 5-2:
'''
You don’t have to limit the number of tests you cre-
ate to 10. If you want to try more comparisons, write more tests and add them

to conditional_tests.py. Have at least one True and one False result for each of
the following:
• Tests for equality and inequality with strings
• Tests using the lower() method
• Numerical tests involving equality and inequality, greater than and less
than, greater than or equal to, and less than or equal to
• Tests using the and keyword and the or keyword
• Test whether an item is in a list
• Test whether an item is not in a list'''

# Soluzione ES. 5-2:

if True:
    food: str = "Lasagna"
    car: str = "Renault"
    thing: str = "hammer"
    num1: int = 19
    num2: int = 123
    cars: list[str] = ["Audi","Bmw","Panda","Alfa Romeo","Cupra","Lotus","Ferrari",]
    
    print("Is thing == 'Panda'? I predict False")
    print(thing == "Panda")
    print("\nIs thing == thing in uppercase ? I predict False")
    print(thing == thing.upper())
    print("\nIs num1 > num2 ? I predict False")
    print(num1 > num2)
    print("\nIs num1*6+9 <= num2 ? I predict True")
    print(num1*6+9 <= num2)
    print("\nIs 'Cupra' in cars ? I predict True")
    print("Cupra" in cars)
    print("\nIs car in car or 'Bmw' in car ? I predict True")
    print(car in car or 'Bmw' in car)
    print("\nIs food == 'Lasagna' and len(food) != len(car) ? I predict False")
    print( food == 'Lasagna' and len(food) != len(car))
    print("\nIs 'hammer' not in cars ? I predict True")
    print("hammer" not in cars)
    
    
    
    

