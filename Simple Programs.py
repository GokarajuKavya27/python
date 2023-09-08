#!/usr/bin/env python
# coding: utf-8

# In[8]:


#Sum of even numbers
sum=0
for i in range(10):
    if i%2==0:
        sum+=i
print(sum)


# In[5]:


#Area of rectangle
l=float(input("enter the length of rectangle:"))
b=float(input("enter the breadth of rectangle:"))
area=(l*b)
print("Area is:",area)


# In[19]:


#To find ASCII values and ASCII characters
a='A'
print(ord(a))
print(ord('u'))
print(chr(45))
print(ord("F"))
print(ord('l'))
print(chr(5))
print(ord('J'))
print(chr(34))
print(ord('K'))
print(chr(89))
print(ord('M'))
print(chr(7))


# In[31]:


#Converstion from Celsius to Fahrenheit
Celsius=float(input("enter temperature in celsius:"))
Fahrenheit=Celsius*(9/5)+32
print(" Temperature in Fahrenheit:",Fahrenheit)


# In[34]:


#Conversion from Fahrenheit to Celsius
Fahrenheit=float(input("enter temperature in Fahrenheit:"))
Celsius=(Fahrenheit-32)*5/9
print(Celsius)


# In[42]:


#Swapping of numbers
a=10
b=23
temp=a
a=b
b=temp
print(a,b)

#Another method
a=34
b=90
a=a+b
b=a-b
a=a-b
print(a,b)
   
#Another method
a=100
b=200
a=a^b
b=a^b
a=a^b
print(a,b)


#Another method
a=44
b=34
(a,b)=(b,a)
print(a,b)


#Another method
a=59
b=38
a=a*b
b=a//b
a=a//b
print(a,b)


# In[44]:


#Check the given number is odd or even
a=int(input("enter the number:"))
if a%2!=0:
    print("the number is odd")
else:
    print("the number is even")


# In[8]:


#To check char is vowel or consonent
vowels=['a','e','i','o','u','A','E','I','O','U']
a=input("eneter a character:")
if a in vowels:
    print("the char is a vowel")
else:
    print("the char is consonents")


# In[12]:


#Another method
def check(x):
    if(x=='a'or x=='e'or x=='i'or x=='o'or x=='u'or x=='A'or x=='E'or x=='I'or x=='O'or x=='U'):
        print("vowels")
    else:
        print("consonents")
check('g')
check('D')
check('i')
check('U')
check('W')
check('o')


# In[2]:


a=input("enter a number:")
b=input("enter a number:")
c=input("enter a number:")
if (a>b) and (a>c):
    print("a is bigger")
elif(b>a) and (b>c):
    print("b is bigger")
else:
    print("c is big")


# In[6]:


#Whether the number is positive or negative
a=int(input("enter a number:"))
if a>0:
    print("positive number")
elif a<0:
    print("negative number")
else:
    print("zero")


# In[13]:


#Checking if the given year is leap year  
def CheckLeap(Year):  
    if ((Year % 400 == 0) or  
       (Year % 100 != 0) and  
       (Year % 4 == 0)):   
        print("Given Year is a leap Year");    
    else:  
        print ("Given Year is not a leap Year")   
Year = int(input("Enter the number: "))  
  
CheckLeap(Year)  


# In[9]:


import calendar

year = int(input("Enter a year: "))

if calendar.isleap(year):
    print(year, " is a leap year")
else:
    print(year, "is not a leap year.")


# In[ ]:




