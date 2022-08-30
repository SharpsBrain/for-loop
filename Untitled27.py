#!/usr/bin/env python
# coding: utf-8

# In[2]:


fruits=["apple", "banana", "cherry"]
for x in fruits:
    print(x)


# In[3]:


for x in "banana":
    print(x)


# In[4]:


#break statement:
fruits=["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x=="banana":
        break


# In[8]:


#break statement:
fruits=["apple", "banana", "cherry"]
for x in fruits:
    if x=="banana":
         print(x)
    if x=="banana":
        break


# In[10]:


#continue statement:
fruits=["apple", "banana", "cherry"]
for x in fruits:
    if x=="banana":
        continue
        print(x)


# In[ ]:




