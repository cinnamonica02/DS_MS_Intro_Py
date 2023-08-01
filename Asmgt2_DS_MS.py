#!/usr/bin/env python
# coding: utf-8

# ### DS MS Asgmt 2

# In[ ]:


### Q1. How do you comment code in Python? What are the different types of comments?



# In[ ]:


#### First most basic way is to use hashes

# Like so ''


# ### You can also use mark down if your coding on a notebook type environment
# #### like myself now :)

# In[ ]:


'''
    I also learned about tripple quotes recently :)
    You can make multiple comments without having to write
    hash mark multiple times!
'''


# In[3]:


### Q2. What are variables in Python? How do you declare and assign values to variables?


### Variables in python unlike other languages are very straight forward
#### and dont need specification (eg, str, int, bool etc)


## you just say 

lst = [1,34,55, 8, 0, 99 , (44.55, 42.33, 22.22, 949.284) 
       ,  'Quiero platano maduro con queso']
## and 'lst' is now the variable we assigned to this list :)



# In[4]:


lst


# In[ ]:





# In[13]:


##### Q3. How do you convert one data type to another in Python?


### one way
str(lst)


### string to interger conversion

string = '12'

str_toint = int(string)


# In[14]:


str_toint


# In[ ]:


### Q4. How do you write and execute a Python script from the command line?












# In[6]:


#### Q5. Given a list my_list = [1, 2, 3, 4, 5]
# write the code to slice the list and obtain the sub-list [2, 3].


my_list = [1, 2, 3, 4, 5]

sliced_list=my_list[1:3]

sliced_list




# In[ ]:


##### Q6. What is a complex number in mathematics
###### and how is it represented in Python?

### Complex numbers are a combination of real and imaginary numbers. 
#### Real part can be expressed through int or decimals while imaginary has
##### a square that is negative. 

### Complex numbers arise from the need to express negative roots which real
#### numbers cant do



### In python complex numbers are denoted using 'j'

## eg.

z = 3 + 2j

a = 3 + (-2j)




# In[ ]:


#### Q7. What is the correct way to declare a variable 
### named age and assign the value 25 to it?

young_folk = 25










# In[ ]:


### Q8. Declare a variable named price and assign the value 9.99 to it.

### What data type does this variable
## belong to?


price_of_markers = 9.99 ## Float












# In[7]:


# Q9. Create a variable named name and assign your full name to it as a string.
### How would you print the  value of this variable?


name = 'Maria Monica Guevara'

name
print(name)



# In[15]:


#### . Given the string "Hello, World!", extract the substring "World".


first_string = 'Hello, World!'

first_string[7:12]



# In[16]:


##### Q11. Create a variable named "is_student" and assign it a boolean value
### indicating whether you are currently a student or not.



is_student = True

print(is_student)




