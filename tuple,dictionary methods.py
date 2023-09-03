#!/usr/bin/env python
# coding: utf-8

# In[23]:


xs = (1, 2, 3, 4, 5)
print(sum(xs))


# In[4]:


c=('aqpple',3,True)
print(c)


# In[5]:


c=('cat','dog','bird','fish')
print(c[1])


# In[11]:


a=(1,2,3)
b=('a','b','c')
print(a+b)


# In[12]:


print(len(a))
print(len(b))


# In[15]:


a=(10,20,30,40,25)
print(25 in a)
print(55 in a)


# In[17]:


a={}
print(a)


# In[18]:


b={"john":25,"max":45}
print(b)


# In[20]:


a={"name":"bob","city":"newyork","age":20}
print(a["name"])
print(a["city"])


# In[22]:


a={"name":"k","age":23}
if ("phone" in a ):
    print("available")
else:
    print(" not available")


# In[40]:


x={"name":"kav","class":3,"university":"bharath"}
x["name"]="kavya"
x["colour"]="red"
print(x)


# In[42]:


print(x.keys())
print(x.values())
print("rollno" in x)
print(x.pop("university"))


# In[48]:


employee={"name":"alice","age":"30"}
print(employee)
employee["age"]=35
print(employee)
employee["colour"]="yellow"
print(employee)
print(employee.pop("age"))
print(employee)


# In[ ]:




