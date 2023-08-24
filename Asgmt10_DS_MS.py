#!/usr/bin/env python
# coding: utf-8

# # Exception Handling Asgmt 2 🫧

# In[ ]:


# Q1. Explain why we have to use the Exception class while 
# creating a Custom Exception.


# Because we are inheriting basic properties from this class


# In[2]:


# Q2. Write a python program to print Python Exception Hierarchy.

# eg

import inspect as ipt

def tree_class(cls, ind =0):
    print('-' * ind, cls.__name__)
    for K in cls.__subclasses__():
        tree_class(K, ind + 3)
print ('inbuilt exception : ')

ipt.getclasstree(ipt.getmro(BaseException))

# function call

tree_class(BaseException)


# In[4]:


# Q3. What errors are defined in the ArithmeticError class? 

# Explain any two with an example.


# ArithmeticError is the base class for a variety of arithmetic errors, 
## eg dividing by 0, or a too large calculation for python/ 
### others include 'overflowerror', 'zerodivision' and 'floatingpoint'

##  Zero division

try:
    arithmetic = 5/0
    print(arithmetic)
except ArithmeticError:
        print('You have just made an Arithmetic error')


# In[2]:


# Q4. Why LookupError class is used? Explain with an example 

# KeyError

try:
    
    details = [ {'name':'James', 'gender':'male','age': 22},
               {'name': 'Peter', 'gender':'male', 'age': 31},
               {'name': 'Jane', 'gender': 'female', 'age': 29}]
    
except KeyError:
    print('Wrong key used')

else: 
    print('Thankyou')
    
    
# IndexError

try:
    countries = ['Canada', 'Albania', 'Belgium']
except IndexError:
    print('wrong index used')
else:
    print('You are welcome')
    


# In[ ]:


# Q5. Explain ImportError. What is ModuleNotFoundError?



# An import error occurs when you try to import a module that has 
## dependencies that are missing or cannot be imported. The error message
### shows the name of the module that caused the import error. 




# When you import a module that doesnt exist or misspell the module name
## Python raises a ModuleNotFoundError . This error occurs when python
### cannot find the specified module. The error message shows the name
#### of the module that Python cannot locate. 






# In[ ]:


# Q6. List down some best practices for exception handling in python.


# 1 back to basic - mastering try,except and finally blocks :)

# 2 Catching specific exceptions - eg






# In[4]:


filename = 'example.txt'

try: 
    with open(filename, 'r') as file:
        data = file.read()
except FileNotFoundError:
    print(f'File not found: {filename}')
except IOError:
    print(f'An I/O error occurred while reading {filename}')
else:
    print(f'Succesfully read data from {filename}')
    
    


# In[6]:


# 3 Raising custom exceptions specific to your use case 

# eg 

class NegativeNumberError(Exception):
    def __init__(self, value):
        self.value = value
        
    def __str__(self):
        return f'Negative numbers are not allowed {self.value}'
    
def process_positive_number(number):
    if number < 0:
        raise NegativeNumberError(number)
    return number * 2

try:
    result = process_positive_number(-5)
except NegativeNumberError as e:
    print(f'An error occurred {e}')


# In[ ]:


# 4 - Common mistakes to avoid 

# > Not specifying exception and going too general

# > Swallowing an exception - catching the exception
## but taking no action to warn the user or fixing it

# > Ignoring Important exceptions - try to anticipate the kinds
## of exceptions that could arise in a given case and use exceptions
### accordingly - eg if you are working with files its prob a good idea
#### to use Filenotfounderror or IOError

# > Take advtg of logging to log exceptions and erors !
## > You can take advantage of the exception() method provided
### by the logging module. This method automatically records the
#### traceback giving you all the information you need to debug the issue






