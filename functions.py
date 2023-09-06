#!/usr/bin/env python
# coding: utf-8

# In[1]:


def cla():
    print("sun raises in the east")
cla()


# In[8]:


def cla(name):
    print("hello" " "+name)
cla("alexa")

#Method-2
def cla(name):
    print(f"hello {name}")
cla("Phani")


# In[12]:


def sum(a,b):
    Sum=a+b
    return(Sum)
sum(10,20)




# In[37]:


def sum(a,b):
    return a+b
r=sum(22,67)
print(r)


# In[16]:


def fan(name="kavya"):
    print(f"holaa {name}")
fan()
fan("Adhi")
          


# In[20]:


def add(a,b):
    return(a+b)
def sub(a,b):
    sub=add(a,b)
    return(sub*2)
sub(30,40)


# In[30]:


a="harry"         #Global variable
def jump():
    b="potter"    #local variable
    print(a)
    print(b)
jump()
print(a)
#shows error when we try to print "b" becoz it is local variable
print(b)


# In[31]:


def greet_user(name="guest"):
    print(f"hello {name}")
greet_user()
greet_user("mummy")
    


# In[35]:


def calculate_sum(a,b,c):
    return a+b+c
r=calculate_sum(33,84,40)
t=calculate_sum(5,10,15)
print(t)
print(r)


# In[42]:


def greet(name,age):
    print(f"Hii {name} and ur Age is {age}")
greet("daya",44)
greet(name="alex",age=69)
greet(age=23,name="bobby")

