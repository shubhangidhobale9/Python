#Assignments -Questions

"""
1. Which of the following is correct with respect to OOP concept in Python?

A. Objects are real world entities while classes are not real.
B. Classes are real world entities while objects are not real.
C. Both objects and classes are real world entities.
D. Both object and classes are not real. 


#A. Objects are real world entities while classes are not real.


2. How many objects and reference variables are there for the given Python code?

class A:
	print("Inside class")
A()
A()
obj=A()

A. 2 and 1
B. 3 and 3
C. 3 and 1
D. 3 and 2

#C. 3 and 1


3. Which of the following is False with respect Python code?

class Student:

	def __init__(self,id,age):

		self.id=id

		self.age=age

std=Student(1,20)

A. "std" is the reference variable for object Student(1,20)
B. id and age are called the parameters.
C. Every class must have a constructor.
D. None of the above

#C. Every class must have a constructor.



4. What will be the output of below Python code?

class Student:

	def __init__(self,name,id):

		self.name=name

		self.id=id

		print(self.id)

std=Student("Simon",1)

std.id=2

print(std.id)

A. 1
    1
B. 1
    2
C. 2
    1
D. 2
    2

#B. 1
    2



5. What will be the output of below Python code?

class A():

	def __init__(self,count=100):

		self.count=count



obj1=A()

obj2=A(102)

print(obj1.count)

print(obj2.count)

A. 100
    100
B. 100
    102
C. 102
    102
D. Error

#B. 100
    102



6. Which of the following is correct?

class A:
    def __init__(self,name):
        self.name=name
a1=A("john")
a2=A("john")
A. id(a1) and id(a2) will have same value.
B. id(a1) and id(a2) will have different values.
C. Two objects with same value of attribute cannot be created.
D. None of the above

#B. id(a1) and id(a2) will have different values.



7. Which of the following is correct?

class A:

	def __init__(self):

		self.count=5

		self.count=count+1

a=A()

print(a.count)

A. 5
B. 6
C. 0
D. Error

#D. Error


8. Which of the following is correct?

class Book:
	def __init__(self,author):
		self.author=author
book1=Book("V.M.Shah")
book2=book1
A. Both book1 and book2 will have reference to two different objects of class Book.
B. id(book1) and id(book2) will have same value.
C. It will throw error as multiple references to same object is not possible.
D. None of the above
View Answer

#B. id(book1) and id(book2) will have same value.

9. In python, what is method inside class?

A. attribute
B. object
C. argument
D. function

#D. function



10. What will be the output of below Python code?

class A:

	def __init__(self,num):

		num=3

		self.num=num

	def change(self):

		self.num=7

a=A(5)

print(a.num)

a.change()

print(a.num)

A. 5
     7
B. 5
     5
C. 3
     3
D. 3
     7

#D. 3
     7

"""

"""
1. To create a class, use the keyword?

A. new
B. except
C. class
D. object

#C. class



2. All classes have a function called?

A. __init__
B. __init__()
C. init
D. init()

@B. __init__()



3. The __________ parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.

A. __init__()
B. self
C. both A and B
D. None of the above

#C. both A and B



4. You can delete properties on objects by using the ______ keyword.

A. delete
B. dedl
C. del
D. drop

#C. del



5. A variable that is defined inside a method and belongs only to the current instance of a class is known as?

A. Inheritance
B. Instance variable
C. Function overloading
D. Instantiation

#B. Instance variable



6. A class variable or instance variable that holds data associated with a class and its object is known as?

A. Class variable
B. Method
C. Operator overloading
D. Data member

#D. Data member


7. What is setattr() used for?

A. To set an attribute
B. To access the attribute of the object
C. To check if an attribute exists or not
D. To delete an attribute


#A. To set an attribute



8. What will be output for the folllowing code?

 class test:
     def __init__(self,a):
         self.a=a

     def display(self):
         print(self.a)
obj=test()
obj.display()
A. Runs normally, doesn’t display anything
B. Displays 0, which is the automatic default value
C. Error as one argument is required while creating the object
D. Error as display function requires additional argument

#C. Error as one argument is required while creating the object



9. _____ represents an entity in the real world with its identity and behaviour.

A. A method
B. An object
C. A class
D. An operator

#B. An object


10. The class has a documentation string, which can be accessed via?

A. ClassName
B. ClassName __doc__
C. __doc__
D. ClassName.__doc__

#D. ClassName.__doc_
"""

