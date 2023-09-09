#!/usr/bin/env python
# coding: utf-8

# In[1]:


#to check even or odd using function
def check(x):
    if x%2==0:
        print("even")
    else:
        print("odd")
check(57)
check(9)
check(14)


# In[4]:


#Factorial of a number
n=int(input("enter the number:"))
p=1
while (n>1):
    p=p*n
    n-=1
print(p)


# In[5]:


#Square of a number 
n=int(input("enter a number:"))
if(n>0):
    a=n*n
print(a)

#another method
n=int(input("enter a number:"))
if(n>0):
    a=n**2
    print(a)
    
    
#Another method    
n= int(input("enter a number:"))
while n>=1:
    a=n**2
    print(a)
    break


# In[6]:


#Square of N numbers
n=int(input("enter a number:"))
for i in range(1,n+1):
    a=i**2
    print(a)


# In[7]:


#Calculate x to the power y
x=int(input("enter a number:"))
y=int(input("enter a number:"))
if x>0:
    a=x**y
    print(a)


# In[8]:


#Multiplication table
a=int(input("enter the number:"))
for i in range(11):
    s=i*a
    print(a,'x',i,'=',s)


# In[10]:


a=int(input("enter a number:"))
sum=0
for i in range(1,a+1):
    sum+=i
print(sum)


#Another method
b=int(input("enter a number:"))
sum=0
while(b>0):
    sum+=b
    b-=1
print(sum)


# In[3]:


n1=1
n2=2
print(n1)
print(n2)
for i in range(1,11):
    n3=n1+n2
    print(n3)
    n1=n2
    n2=n3


# In[6]:


a=str(input("enter a number:"))
b=a.upper()
s=a.lower()
print(b)
print(s)


# In[ ]:




