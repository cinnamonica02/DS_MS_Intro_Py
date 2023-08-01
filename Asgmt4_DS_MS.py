#!/usr/bin/env python
# coding: utf-8

# In[13]:


### Q1. Create a python program to sort the given list of tuples 
## based on integer value using a lambda function.

char_lst = [('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), 
             ('Jack Kallis', 25534), ('Virat Kohli', 24936)]

print(char_lst)




# In[14]:


char_lst.sort(key = lambda x: x[1])


# In[15]:


print(char_lst)


# In[18]:


### Q2. Write a Python Program to find the squares of all the numbers
## in the given list of integers using lambda and map functions.



num_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


square_num_lst = list(map(lambda num: num ** 2, num_lst))

print(square_num_lst)




# In[11]:


##### Q3. Write a python program to convert the given list 
### of integers into a tuple of strings. Use map and lambda functions

lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Expected output: ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')

str_lst = list(map(lambda x: str(x), lst1))

print(str_lst)

def to_tpl(str_lst):
    return tuple(str_lst)

print(to_tpl(str_lst))


# In[19]:


#### Q4. Write a python program using reduce function to compute the product 
## of a list containing numbers from 1 to 25.


from functools import reduce

iter=list(range(1,26))


print(iter)

reduce(lambda x, y: x*y , iter)


# In[35]:


#### Q5. Write a python program to filter the numbers in a given list
# that are divisible by 2 and 3 using the filter function.



num_lst = [2, 3, 6, 9, 27, 60, 90, 120, 55, 46]

  
list(filter(lambda x:x %3 ==0 and x % 2 == 0, num_lst))








# In[36]:


### Q6. Write a python program to find palindromes 
## in the given list of strings using lambda and filter
#  function.



str_lst = ['python', 'php', 'aba', 'radar', 'level']


is_palindrome = list(filter(lambda x: (x == "".join(reversed(x))), str_lst))


print(is_palindrome)

