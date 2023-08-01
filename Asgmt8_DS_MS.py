#!/usr/bin/env python
# coding: utf-8

# # OOPs Asgmt 2 😶‍🌫️

# In[6]:


class Vehicle:
    def __init__(self, name_of_vehicle, max_speed, avg_of_vehicle):
        self.name_of_vehicle = name_of_vehicle
        self.max_speed = max_speed
        self.avg_of_vehicle = avg_of_vehicle

    def show(self):
        print(f"{self.name_of_vehicle} runs at {self.max_speed} and averages a speed of {self.avg_of_vehicle}")

        # Q2. Create a child class car from the vehicle class created 
## in Q1, which will inherit the vehicle class.

class VehicleChild(Vehicle):
    
    def which_vehicle(self):
        print(f"{self.name_of_vehicle} runs at {self.max_speed} and averages a speed of {self.avg_of_vehicle}")


    
v = Vehicle('Tesla', 1242, 10000)
v_d = VehicleChild('Honda', 39247, 1000)

v.show()
v_d.which_vehicle()





# In[4]:


class Vehicle:
    def __init__(self, name_of_vehicle, max_speed, avg_of_vehicle):
        self.name_of_vehicle = name_of_vehicle
        self.max_speed = max_speed
        self.avg_of_vehicle = avg_of_vehicle

    def show(self):
        print(f"{self.name_of_vehicle} runs at {self.max_speed} and averages a speed of {self.avg_of_vehicle}")

    def seating_capacity(self, capacity):
        return f"{self.name_of_vehicle} has a seating capacity of {capacity}"


v = Vehicle('Tesla', 1242, 10000)
v.show()
print(v.seating_capacity(5))



# In[10]:


# Q4. What are getter and setter in python? Create a class and create a getter and a setter method in this
## class.


## Getter - Method that allows you to access an attribute in a given class


## Setter - A method that allows you to set or mutate the value of an attribute 

## If an attribute is likely to change its internal implementation then you should use
# getter and setter methods

# Eg

class chocolatecake:
    def __init__(self, recipe_price, recipe_amount):
        self.__recipe_price = recipe_price
        self.recipe_amount = recipe_amount
        
    @property
    def recipe_price_access(self):
        return self.__recipe_price
    

    # Using set property to allow user to access values on protected / public prop
    
    @recipe_price_access.setter
    def recipe_price_ser(self, price):
        if price <= 50:
            pass
        else: 
            self.__recipe_price = price
            
    @recipe_price_access.deleter
    def recipe_price_del(self):
        del self.__recipe_price


chck = chocolatecake(35 , 1 )
chck.recipe_amount
chck._chocolatecake__recipe_price


# In[11]:


# Q5.What is method overriding in python? Write a python code to demonstrate method overriding.

## Method overriding refers to defining a method in a subclass that has the same name as the 
## one in its super class. It allows a subclass to provide its own implementation of a method
## defined in its superclass


# Eg

class Animal:
    def speak(self):
        print('Animal speaking!')
class Dog(Animal):
    def speak(self):
        print('Dog barking')
obj = Dog()
obj.speak()


# In[21]:


class Human:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

h001 = Human('Abhay', 'Kashyap', 26)


# In[ ]:




