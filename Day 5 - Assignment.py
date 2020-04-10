#!/usr/bin/env python
# coding: utf-8

# # List Slicing
# CHAITANYA V

# In[12]:


#Establishing the list using for loop and range function.


list_1=[]
for i in range(1,51):
    list_1.append(i)
print(list_1)


# In[13]:


# User inputs the start index as "a".

a=int(input("Enter the start index "))


# In[14]:


#User inputs the end index as "b".


b=int(input("Enter the end index "))


# In[15]:


# Using for loop again to print the output within the range of the given input from the established list.

for i in range(a,b):
  print(list_1[i],end=" ")


# # Dictionary data structure

# In[25]:


# Using for loop to generate a dictionary with the help of the user's input.


res={}
x= int(input("Enter the number here "))
for i in range(1,x+1):
    res[i]=i*i
print (res)
    



# # ------DAY 5 - Assignment------

# In[ ]:




