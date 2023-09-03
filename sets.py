#!/usr/bin/env python
# coding: utf-8

# In[15]:


set={1,2,3,4}
set.add(55)
set.add(67)
print(set)
a=set.discard(99)
print(set)
b=set.remove(2)
print(set)


# In[16]:


b=set.pop()
print(b,set)


# In[29]:


a={1,2,3,4}
b={6,2,7,8,9}
print(b.union(a))
print(a.intersection(b))
print(b.difference(a))
print(a.symmetric_difference(b))
print(3 in b)
print(2 in a)
print(3 not in b)


# In[ ]:




