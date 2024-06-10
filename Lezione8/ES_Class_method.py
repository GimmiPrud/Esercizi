
# Giammarco Prudenzi
# Esercizi su classi astratte, class methods e static methods

# ES.1: Creating an Abstract Class with Abstract Methods:
'''
Create an abstract class Shape with an abstract method area and another abstract method perimeter.
Then, create two subclasses Circle and Rectangle that implement the area and perimeter methods.
'''
# Svolgimento ES. 1:

if True:
    
    from abc import ABC, abstractmethod
    
    class Shape(ABC):
        
        @abstractmethod
        def area(self):
            pass
        
        @abstractmethod
        def perimeter(self):
            pass
        
    class Circle(Shape):
        
        def __init__(self, radius: float):
            super().__init__()
            self.radius = radius
            
        def area(self):
            area_circle = (self.radius**2)* 3.14
            return f"Area circle = {round(area_circle,2)}"
            
        def perimeter(self):
            perimter_circle = ( 3.14 * 2)* self.radius
            return f"Perimeter circle = {round(perimter_circle,2)}"
            
    class Rectangle(Shape):
        
        def __init__(self, b: float, h: float):
            super().__init__()
            self.b = b
            self.h = h
        
        def area(self):
            area_rectangle = self.b*self.h
            return f"Area rectangle = {round(area_rectangle,2)}"
        
        def perimeter(self):
            perimeter_rectangle = (self.b*2) + (self.h*2)
            return f"Perimeter rectangle = {round(perimeter_rectangle,2)}"
        
    
    cerchio1 = Circle(5)
    print(cerchio1.area())
    print(cerchio1.perimeter())
    
    rectangle1 = Rectangle(15, 8)
    print(rectangle1.area())
    print(rectangle1.perimeter())
