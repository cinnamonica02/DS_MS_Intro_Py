#!/usr/bin/env python
# coding: utf-8

# # OOPs Asgmt 1 👍

# In[7]:


# Q1. Explain Class and Object with respect to Object-Oriented Programming. 

## Give a suitable example.

### A class is an entitity or blueprint with many aspects to it
#### an object is an instance of this blueprint for eg.


# eg 1
class test:
    pass

a = test()

# eg 2

class girls_that_code_academy:
    
    def __init__(self, phone_num , email, student_id):
        
        self.phone_num = phone_num
        self.email = email
        self.student_id = student_id
        
    def return_student_details(self):
        return self.phone_number, self.email, self.student_id
    
    Melisa = girls_that_code_academy(2525987, 'meliosorio@gmail.com', 'ID2345')
    print(Melisa.phone_num)


# In[13]:


# Q2. Name the four pillars of OOPs.

## OOPs stands for Object oriented programming and the main 4 principles of OOPs are 


### Encapsulation - To enclose smt in - as in a pill type capsule

## We make the use of privat e variables using __ when defining attributes in self
### or alternatively as per the update in @dataclass we can pass in the 
#### '(frozen=True)' argument to keep out variables inmutable


### Inheritance

## Allows us to define class that inherits methods and properties from another class. 
### eg. child and parent

# Eg. 

class Family:
    def __init__(self, family_name, num_of_members, country):
        self.family_name = family_name
        self.num_of_members = num_of_members
        self.country=country
        
    def member_says(self):
        print(f'Hey, I am from {self.family_name} family and there are {self.num_of_members} members in my family')
        
class Family_detailed(Family):
    
    def which_country(self):
        print(f'The {self.family_name} famimly hasa roots in {self.country}')
        
a = Family('Dominguez', 5, 'Colombia')
b = Family_detailed('Cunningham', 7, 'US')

a.member_says()
b.member_says()
b.which_country()

### Polymorphism

## Refers to the usage of a single method / op to represent different types in
### different scenarios.


# Eg

class Class1():
    def pt(self):
        print('This function determines class 1')
        
        
class Class2():
    def pt(self):
        print('This function determines class 2')
        
obj1 = Class1()
obj2 = Class2()

for type in (obj1, obj2): 
    type.pt()



### Abstraction

### Hides internal implementations of a process or method from the user. In this way, the user
#### knows what they do but not how it is done. 


### In python a method becomes abstract when decorated with keyword @abstractmethod

# Eg.

from abc import ABC, abstractmethod

class Company(ABC): # the abstract base class
    
    def work(self): # def the abstract method
        pass
    
class Manager(Company):
    
    def work(self):
        print('I assign work to and manage team')
        
class Employee(Company):
    
    def work(self):
        print('I complete the work assigned to me')
        
# Driver Code

Rob = Manager()
Rob.work()

Katy = Employee()
Katy.work()



# In[15]:


# # Q3. Explain why the __init__() function is used. Give a suitable example.


# This method is known as the constructor method, it is automatically called when a new
## instance (object) is created. 

# Allows us to initialize attributes (variables) of an object

# Eg

class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
        
    def show(self):
        print(self.name, ' teaches', self.subject)
        
T = Teacher('Pat Loeber', 'Calculus') #init is invoked here
T.show()
            
            







# In[ ]:


# Q4. Why self is used in OOPs?

### Self represents the instance of a class
## It allows you to access variables, attributes, and methods of a defined
#  class in python. 

# It is often used with __init__() method and it is the first parameter used.



# In[4]:


# # Q5. What is inheritance? Give an example for each type of inheritance.





### The types of inheritance in python are Single inheritance 

## - Single inheritance is where there is only one base class and one child class in python

# - Eg




## Multilevel inheritance. 

# - Where classes are derived from multiple base classes. 

# Eg
# Base class

class Father:

    def function_1(self):
        print ('I am father.')

# Child class

class Children(Father):

    def function_2(self):
        print ('I am son.')

object = Children()
object.function_1()
object.function_2()
# Base class 1:

class A:
    aname= 'idkhername'
    
    def aclass(self):
        print(self.aname)

# Base class 2:

class B:
    
    bname = ''
    
    def bclass(self):
        print(self.bname)
        
# Child class 🚼

class C(A,B):
    def cname(self):
        print('B:',self.bname)
        print('A:',self.aname)


s1 = C()
s1.bname = 'Anna'
s1.aname = 'Varenko'
s1.cname()



# In[ ]:




