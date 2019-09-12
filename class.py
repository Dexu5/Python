import logging


logging.basicConfig(level=logging.DEBUG)
"""

class myClass: #Defined the class
	x = 5 #Declared and Initialized an Object

p1 = myClass() #Created Class Object
print(p1.x) #Printing the value from Class Object.

"""

class Person:
	def __init__(self, name, age): #Constructor
		self.name = name
		self.age = age

	def met(self):
		print("My name is " + self.name)


#p1 = Person("Kunal", 10)
p2 = Person("Kunal", 20)
#print(type(p2.name))
#print(type(p1.age))

p2.met()




