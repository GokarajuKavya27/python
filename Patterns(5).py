#!/usr/bin/env python
# coding: utf-8

# In[1]:


for i in range(3):
    for j in range(3):
        print("*",end=" ")
    print()       


# In[3]:


for i in range(4):
    for j in range(i+1):
        print("$",end=" ")
    print()
    


# In[4]:


temp=3
for i in range(1,5):
    for j in range(temp):
        print(" ",end=" ")
    for k in range(2*i-1):
        if k%2==0:
            print("*",end=" ")
        else:
            print("$",end=" ")
    temp-=1
    print()
    


# In[5]:


temp=3
for i in range(2,5):
    for j in range(1,i):
        print(i*j,end=" ")
    print()
for i in range(5,7):
    for j in range(1,temp):
        print(i*j,end=" ")
    temp-=1
    print()


# In[6]:


for i in range(5):
    for j in range(5):
        if(i==0 or j==0 or i==4 or j==4):
            print("#",end=" ")
        elif(i==1 or j==1 or i==3 or j==3):
            print("$",end=" ")
        else:
            print("?",end=" ")
    print()


# In[ ]:




