
# Giammarco Prudenzi
# Esercizi su classi astratte, class methods e static methods

# ES. 1: Creating an Abstract Class with Abstract Methods:
'''
Create an abstract class Shape with an abstract method area and another abstract method perimeter.
Then, create two subclasses Circle and Rectangle that implement the area and perimeter methods.
'''
# Svolgimento ES. 1:

if False:
    
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
    
    
# ES. 2: Implementing Static Methods
'''
Create a class MathOperations with a static method add that takes two numbers and returns their sum,
and another static method multiply that takes two numbers and
returns their product.
'''
# Svolgimento ES. 2:

if False:
    
    class MathOperations:
        
        @staticmethod
        def add(num1: int, num2: int):
            return f"sum of this numbers is: {num1+num2}\n"
        
        @ staticmethod
        def multiply(num1: int, num2: int):
            return f"multiply of this number is: {int(num1*num2)}\n"
        
        
        print(add(25,25))
        print(multiply(25,25))
        

# ES. 3: Library Management System 
'''
Create a Book class containing the following attributes: title, author, isbn
The book class must contains the following methods:

__str__ method to return a string representation of the book.

@classmethod from_string(cls, book_str) to create a Book instance from a string in the format "title, author, isbn".
It means that you must use the class reference cls to create a new object of the Book class using a string.

Example: 
book = “La Divina Commedia, D. Alighieri, 999000666”
divina_commedia: Book = Book.from_string(book)
Here divina_commedia must contain an instance of the class Book with 
title = La Divina Commedia, author = D. Alighieri, isbn = 999000666

Create a Member class with the following attributes: name, member_id, borrowed_books
The member class must contain the following methods:
borrow_book(book) to add a book to the borrowed_books list.
return_book(book) to remove a book from the borrowed_books list.
__str__ method to return a string representation of the member.
@classmethod from_string(cls, member_str) to create a Member instance from a string in the format "name, member_id".

Create a Library class with the following attributes: books, members, total_books (class attribute to keep track of the total number of books)
The library class must contain the following methods:
add_book(book) to add a book to the library and increment total_books.
remove_book(book) to remove a book from the library and decrement total_books.
register_member(member) to add a member to the library.
lend_book(book, member) to lend a book to a member. It should check if the book is available and if the member is registered.
__str__ method to return a string representation of the library with the list of books and members.
@classmethod library_statistics(cls) to print the total number of books.

Create a script and play a bit with the classes:
Create instances of books and members using class methods. Register members and add books to the library.
Lend books to members and display the state of the library before and after lending.
'''       
# Svolgimento ES. 3:

if True:
    
    class Book:
        def __init__(self, title: str, author: str, isbn: int):
            self.title = title
            self.author = author
            self.isbn = isbn
        
        def __str__(self) -> str:
            return f"book = {self.title},{self.author},{self.isbn}"
        
        @ classmethod
        def from_string(cls, book_str):
            pass



# ES. 4 University Management System
'''
Create a system to manage a university with departments, courses, professors, and students. 
Create an abstract class Person:
Attributes:
name (string)
age (int)
Methods:

__init__ method to initialize the attributes.
Abstract method get_role to be implemented by subclasses.
__str__ method to return a string representation of the person.
Create subclasses Student and Professor that inherit from Person and implement the abstract methods:

Student:
Additional attributes: student_id (string), courses (list of Course instances)
Method enroll(course) to enroll the student in a course.
Professor:
Additional attributes: professor_id (string), department (string), courses (list of Course instances)
Method assign_to_course(course) to assign the professor to a course.

Create a class Course:
Attributes:
course_name (string)
course_code (string)
students (list of Student instances)
professor (Professor instance)
Methods:

__init__ method to initialize the attributes.
add_student(student) to add a student to the course.
set_professor(professor) to set the professor for the course.
__str__ method to return a string representation of the course.
Create a class Department:

Attributes:
department_name (string)
courses (list of Course instances)
professors (list of Professor instances)

Methods:
__init__ method to initialize the attributes.
add_course(course) to add a course to the department.
add_professor(professor) to add a professor to the department.
__str__ method to return a string representation of the department.
Create a class University:

Attributes:
name (string)
departments (list of Department instances)
students (list of Student instances)

Methods:
__init__ method to initialize the attributes.
add_department(department) to add a department to the university.
add_student(student) to add a student to the university.
__str__ method to return a string representation of the university.

Create a script:
Create instances of departments, courses, professors, and students.
Add them to the university.
Enroll students in courses and assign professors to courses.
Display the state of the university.
'''
# Svolgimento ES. 4:

            
            
            
            
