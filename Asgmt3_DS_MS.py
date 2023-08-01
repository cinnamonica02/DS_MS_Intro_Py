#!/usr/bin/env python
# coding: utf-8

# ### Functions

# In[4]:


### Q1. Which keyword is used to create a function? 
###Create a function to return a list of odd numbers in the
###range of 1 to 25.

for i in range(1,25):
    return i if i %2!= 0

### Errors
    
### Syntax

## return cannot be used to exit a dunction and provide value
### Instead loop should be inside function.

### Logic

### Loop will exit once it checks first odd value (1)






# In[14]:


#### To fix this we can define a function first, accumulate odd numbers 
##### in a list and return list

def get_odd_nums():
    odd_nums = []
    for i in range(1,25):
        if i % 2 != 0:
            odd_nums.append(i)
    return odd_nums


# In[17]:


result = get_odd_nums()
result


# In[20]:


#### Q2. Why *args and **kwargs is used in some functions? 
### Create a function each for *args and **kwargs to
### demonstrate their use.



# In[28]:


### args basically means we will be able to get any number of arguments
#### in a function

def cats(*args):
    return args


# In[29]:


### for eg
cats(2)


# In[30]:


cats(1,2,3,4,5)


# In[31]:


cats('suju', 'kpop' , [1,2,3,3,4], (12.23, 4.3, 590))


# In[32]:


### And similarly 'kwargs' pass in n number of inputs
#### as arguments but in the form of key and value pair :3 (dict)

def kyungsoo(**kwargs):
    return kwargs


# In[33]:


kyungsoo()


# In[34]:


type(kyungsoo())


# In[42]:


### Eg

def exo(**kwargs):
    for i in kwargs.keys():
        if type(kwargs[i]) == tuple:
            return i, [i]


# In[43]:


exo(a=24, c= [1,23,45,99], s= ('Sehun', 'DO', 'Suho'), b= 33)


# In[ ]:


### Q3. What is an iterator in python?

## An iterator is an object which can be iterated upon.



# In[ ]:


### Name the method used to initialise the iterator object 
## and the method
#### used for iteration. 


### There are several ways (prob better maybe but )

#### according to what we saw in the lectures we can use generator functions
##### to iterate over n 


#### It can also be done using the iter() method and the next() method 
## to return the next value


# In[47]:


### Use these methods to print the 
### first five elements of the given list :  [2, 4, 6, 8, 10, 12, 14, 16,18, 20].


lst =  [2, 4, 6, 8, 10, 12, 14, 16,18, 20]

def first_five(lst):
    a = lst[:5]
    for i in lst:
        yield a
        break
        
    


# In[48]:


for i in first_five(lst):
    print(i)


# In[51]:


### Q4. What is a generator function in python? 

## Why yield keyword is used? Give an example of a generator  function.


### A generator function is a function that will iterate over n, 10x
#### the 'yield' keyword gives record of iterations when called.

## Eg

def test_fib(n):
    a,b = 0,1
    for i in range(n):
        yield a       ## gives the record of iterations gen when called
        a,b = b, a+b
        


# In[52]:


test_fib(10)


# In[53]:


for i in test_fib(10): 
    print(i)


# In[ ]:


def get_odd_nums():
    odd_nums = []
    for i in range(1,25):
        if i % 2 != 0:
            odd_nums.append(i)
    return odd_nums



# In[ ]:


result = get_odd_nums()
result


# In[105]:


### Q5. Create a generator function for prime numbers less than 1000.

### Use the next() method to print the first 20 prime numbers.

def is_prime(num):
    prime_num=[]
    for i in range(1,1000):
        if num % i == 0 and num > i:
            prime_num.append(i)
        return prime_num


# In[106]:


def prime_nums():
    for num in range(1000):
        if is_prime(num):
            yield num


# In[107]:


generator = prime_nums()


# In[104]:


for _ in range(20):
    prime = next(generator)
    print(prime)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




