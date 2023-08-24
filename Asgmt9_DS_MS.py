#!/usr/bin/env python
# coding: utf-8

# # Exception Handling Asmt 1 🚨

# In[ ]:


# What is an Exception in Python?

# An exception is an error that happens during the execution of a program. 

## Whenever there is an error python generates an exception that
# could be handled. 

## Write the difference bween exceptions and syntax errors

# An exception is an event that occurs during the program execution
# and disrupts the normal flow of the programs execution. Errors mostly
# happen at compile time like syntax error however it can happen at 
# runtime aswell 


# In[ ]:


## What happens when an exception is not handled?

# The program will crash


# In[ ]:


# Please explain with an example the following:

## Try and else

# Try block - lets you test a block of code for errors

# except block - Let you handle the error

# else block - lets you execute the code w no error


# finally - Lets you execute the code regardless of the prev


# raise


## Eg 

try:
    f = open('test.txt', 'w')
    f.write('this is my message')
except Exception as e:
    print('there is some issues w the code', e)
else: 
    f.close()
print('this block will execute once try will execute itself w/out exception')



    


# In[1]:


## Eg 2

try:
    f = open('test.txt', 'w')
    f.write('this is my msg')
    # f.close()
except Exception as e:
    print('there is some issues w my code', e)
else:
    f.close()
print('this block will execute once try will execute itself w/out excpt')



# In[ ]:


## *** falta finally 


# In[ ]:


## What are customs exceptions in Python? Why do we need custom exceptions
# Please explain with an example.


# Custom exceptions are used in situations where you want to handle 
## specific errors in your program. Eg, 'FileNot found' , however you 
### may want to handle this exception differently as to how it is 
#### handled traditionally 



# In[3]:


# Create a custom exception class. Use this class to handle exception. 


## 1 Eg - Age exception

age = int(input('enter your age'))

## In our particular case age cant be neative


# First we create the constructor -

class validateage(Exception):
    def __init__(self, msg):
        self.msg = msg
        

# Now we define a function to raise 
## our exception

def validate_age(age):
    if age < 0:
        raise validateage('age should not be lesser than 0')
    elif age > 200:
        raise validateage('age is too high')
    else:
        print('age is valid')
        

try:
    age = int(input('enter your age'))
    validate_age(age)
except validateage as e:
    print(e)






# In[4]:


## Eg 2 - Custom exceptions using traceback

import traceback

class CustomException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.traceback = traceback.format_exc()
        
try:
    raise CustomException('This is a custom exception')
except CustomException as e:
    print(e)
    print(e.traceback)


# In[6]:


## Eg - Custom exception using error code

class CustomException(Exception):
    def __init__(self, message, code):
        super().__init__(message)
        self.code = code
        
try:
    raise CustomException('This is a custom exception', 404)
except CustomException as e:
    print(f'{e} (Error code : {e.code} )')


# In[ ]:




