# varibles in python and differnet data types
a = 28 # interger 
b = 1.5 # float
c="Hello!" #string type
e = True # boolen type
f = None # None type 

# taking user input dinamically
name = input("Enter your name: ")
print(name)

#concatinating the strings.
print("Hello, " + name + "!")

#formatting the strings
print(f"Hello, {name}!")

#checking the type of the variable.
print(type(a))
print(type(b))
print(type(c))

#conditional statements in python.
n = int(input("Enter a number:")) # input function is always a string type
if n > 0:
    print("n is positive")
elif n < 0:
    print("n is negative")
else:
    print("n is zero")

# type casting in python
x = float(input("Enter x: "))
y = float(input("Enter y: "))
z = int(y) # here we converted the float type to the integer type
print(f"x/y = {x/y}")

# sequences in python 
name ="Harry"
print(name[0]) # it help us to index the 0th element in the string
print(name[1]) # it help us to index the 1st element in the string

# Data sctructures in python like list,tuple,set,dict
# list in a python we add remove elements
names = ["Harry", "Ron", "Hermione"]
print(names)
print(names[0])
print(names.append("salauddin"))
print(names.sort()) # to sort the values in python

#tuple in a python which is in-mutable "tuple"
coordinate = (10.0, 20.0)
print(coordinate)

#set in a python which is a collection of unique elements and un oredered "set"
s = set()
s.add(1)
s.add(2) 
s.add(3)
s.add(4)
s.remove(2) # here removed the element from the set using the value from the set
print(len(s)) # findig the length of the set
print(s)

#dictionary in a python its collections of key value pairs where we can use "dict' it help us to map the values
houses = {"Harry": "Gryffindor", "Draco": "Slytherin"}
print(houses["Harry"])
houses["Hermione"] = "Gryffindor"
print(houses["Hermione"])
print(houses.keys())

#loops in python
for i in [0, 1, 2, 3, 4, 5]:
    print(i,end="")
for j in range(6): # range always ends with n-1 length so 5 elements only printed from the 
    print(j,end="")
names = ["Alice", "Bob", "Charlie"]
for name in names:
    print(name) # here we are printing the names in the list

#functions in python which help us to take input and produce the output
from pythonfunctions import square # importing the python  square  from pythonfunctionsr file or module
for i in range(10):
    print(f"The square of {i} is {square(i)}")

# creating the classes in python and objects in the class
class new :
    def __init__(self, name): # here we are creating the constructor in the class
        self.name = name 
    def greet(self):
        print(f"Hello, {self.name}!")
        # creating the object of the class
p = new()
p.name = "Harry"
p.greet()
 
# creating python program to add passengers to the filght based on avilable seats ...

class Flight:
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
    def add_passenger(self, name):
        if not self.open_seats(): # here we are checking the number of seats which are available in the 
            return False
        self.passengers.append(name)
        return True
    def open_seats(self):
        return self.capacity - len(self.passengers)
    
flight = Flight(3)
people = ["Harry", "Ron", "Hermione", "Ginny"]
for person in people:
    if flight.add_passenger(person):
        print(f"Added {person} to flight successfully.")
    else:
        print(f"No available seats for {person}.")

# creating the decorators in python .. it is a function work as a function for a function..
def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Done with the function.")
    return wrapper
@announce
def hello():
    print("Hello, world!")
hello()

# creating lambda functions in the python which is known as anynomous functions
people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]
people.sort(key=lambda person:person['name'])
print(people)

# creating the exception handling in python
import sys
x = int(input("X:"))
y = int(input("Y:"))
print(x/y)
try:
    print(x/y)
except ZeroDivisionError:
    print("Error: Cannot divide by 0.")
    sys.exit(1) # to exit from the programm
finally:
    print("Division is done.")

# creating other exceptions in the python
import sys
try:
    x = int(input("X:"))
    y = int(input("Y:"))
except ValueError:
    print("Error: Invalid input.")
    sys.exit(1)
try:
    result = x/y
except ZeroDivisionError:
    print("Error: Cannot divide by 0.")
    sys.exit(1)
print(f"{x}/{y} = {result}")


 



