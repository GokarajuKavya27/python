#!/usr/bin/env python
# coding: utf-8

# In[1]:


n=1
while n<=10:
    print(n)
    n+=1


# In[2]:


n = int(input("enter a number: "))
i = 1
sum = 0
while (i <= n):
    sum = sum + i
    i = i + 1
print("The sum is: ", sum)


# In[3]:


for i in range(1,6):
    print(i)


# In[5]:


sum=0
for i in range(1,11):
    sum+=i
print(sum)


# In[10]:


str=input("enter:")
l=str.upper()
p=len(l)
print(l)
print(p)


# In[ ]:


n=int(input("enter a number:"))
sum=0
while n>=5:
    sum+=n
    n+=1
print(sum)


# In[ ]:


n=int(input("enter a number:"))
sum=0
while n>=5:
    sum+=n
    n+=1
print(sum)


# In[16]:


str=input("enter:")
l=str.isalpha()
print(l)


# In[18]:


s="h  ii"
p=s.strip()
print(p)


# In[21]:


for i in range(5):
    for j in range(5):
        print("*",end="")
    print()


# In[28]:


for i in range(1,6):
    for j in range(1,6):
        print(i*j,end=" ")
    print()


# In[38]:


for i in range(1,6):
    if i==5:
        break
    print(i)
          
    


# In[39]:


a="python"
b="Python"
if a==b:
    print("true")
else:
    print("false")


# In[43]:


s=input("enter:")
if s==" ":
    print("true")
else:
    print("false")


# In[45]:


l=[1,2,3,4]
print(l[0])
print(l[1])
print(l[2])
print(l[3])


# In[60]:


l=["k","a","v"]
m=' '.join(l)
print(m)


# In[ ]:




