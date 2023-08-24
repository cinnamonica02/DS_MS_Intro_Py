#!/usr/bin/env python
# coding: utf-8

# # Multithreading Asgmt 1 🪡

# In[ ]:


# Q1 What is multithreading in python? Why is it used? 

# The goal of multithreading is to complete multiple tasks at the
# same time. Multithreading in python allows the concurrent and parallel
# occurrence of various tasks. Reducing time and response increasing 
# performance 



# Name the module used to handle threads in python


# The module 'thread' treats a thread as a function, while the module 
# 'threading' is implemented in an OOP way, eg every thread corresponds
# to that obj. The 'thread' module nicely encapsulates threads




# In[ ]:


# Q2 Why threading module used? Write the use of the following functions

# 1. activeCount() - returns the number of threads objects currently active
# The returned count is equal to the length of the list returned by 
# enumerate()

# 2. currentThread() - returns the current thread object corresponding to
# the callers thread of control, if the thread of control was not created
# thru the threading module a dummy thread obj is returned


# 3. enumerate() - returns a list of all thread obj currently active. 
# List include dummy threads and daemonic threads created by current_thread 




# In[ ]:


# Q3 3. Explain the following functions

# 1. run() methods invokes the callable obj passed to the obj constructor
# as the target arg. 


# In[2]:


# Eg 

from threading import Thread
t = Thread(target=print, args=[1])
t.run()

t = Thread(target=print, args=(1,))
t.run()


# In[ ]:


import threading
import time

class CPUPainter:
    def paintwall(self):
        time.sleep(2)
        print('wall painted')
        
    def __init__(self):
        t = threading.Thread(target=self.paintwall)
        t.start()
        
CPUPainter()
CPUPainter()
CPUPainter()
CPUPainter()


# In[ ]:


# 2. start() - starts the thread activity. 
    # Must be called at most once per thread obj. 
    # Arranges for the obj run() method to be invoked in a separate thread
    # of control. Will race a 'RuntimeError' if called more than 1 on 
    # the same thread obj. 

    
# 3. join() waits until the thread terminates , as join alwas returns none
#  isAlive() must be called after join() to decide wether a timeout 
# happened. A thread can be joined many times. 



# In[13]:


# Q4 Write a python program to create two threads. 


# Thread one must print the list of squares and thread two must print 
# the list of cubes





# In[10]:


import threading
import time

class Thread1:
    def listSquares(a, b):
        list= []
        for count in range (a,b):
            list.append(count**2)
            return list
    def __init__(self):
        t = threading.Thread(target=self.listSquares)
        t.start()

class Thread2:
    def listCubes(a,b):
        list=[]
        for count in range (a,b):
            list.append(count**3)
            return list
    def __init__(self):
        t = threading.Thread(target=self.listCubes)
        t.start()

listSquares()

listCubes()


# In[12]:


import threading

class Thread1:
    def listSquares(self, a, b):
        result = []
        for count in range(a, b):
            result.append(count**2)
            print('List of squares:' , result)
        
    def __init__(self, a, b):
        t = threading.Thread(target=self.listSquares, args=(a,b))
        t.start()
        
class Thread2:
    def listCubes(self, a, b):
        result = []
        for count in range(a,b):
            result.append(count**3)
        print('List of Cubes:', result)
        
    def __init__(self, a, b):
        t = threading.Thread(target=self.listCubes, args=(a,b))
        t.start()
        
# Create instances of the Thread1 and Thread 2 classes

a, b = 1, 6

thread1 = Thread1(a,b)

thread2 = Thread2(a, b)    
    


# In[ ]:


# Q5 State advantages and disadvantages of multithreading

# Some advantages include faster code and more optimized used 
# of compute, some disadvantages include increasing complexity
# of the program. constructing and keeping threads in sync is CPU 
# / mmry intensive , diff to debug and unpredictable.



# In[ ]:


# Q6. Explain deadlocks and race conditions.

# A race condition occurs when two threads use the same variable at a given
# time. 

# Deadlock exists when two threads seek one lock simultaneously. Both threads
# will stop  processing or executing fucntions.



# In[14]:


# Eg - Race condition 


from threading import Thread
from time import sleep

counter = 0

def increase(by):
    global counter
    
    
    local_counter = counter
    local_counter += by
    
    
    sleep(0.1)
    
    
    counter = local_counter
    print(f'counter={counter}')
    
    
    
# Creating threads

t1 = Thread(target=increase, args=(10,))
t2 = Thread(target=increase, args=(20,))


# Starting the threads

t1.start()
t2.start()

# Wait for the threads 


# wait for the threads to complete
t1.join()
t2.join()


print(f'The final counter is {counter}')








# In[ ]:





# In[ ]:




