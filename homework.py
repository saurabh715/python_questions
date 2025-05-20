#!/usr/bin/env python
# coding: utf-8

# In[5]:


#question 1
i=int(input("enter the unit from the user="))

if i<=100:
    print("bill of the user is",bill)
elif (i<=200):
    bill=(i-100)*5
    print("bill of the user is",bill)
else:
    bill=(100*5)+(i-200)*10
    print("bill of the user is",bill)
    


# In[ ]:


#Question2
i=int(input("enter your number"))

if   i>90:
    print("grade is A")
elif i>80<=90:
        print("grade is B")
elif i>=60<=80:
        print("grade is C")
elif i<60:
            print("grade is D")
else:
            print("fail")


# In[1]:


#question 3
a = int(input("Enter age of person 1: "))
b = int(input("Enter age of person 2: "))
c = int(input("Enter age of person 3: "))
d = int(input("Enter age of person 4: "))

youngest = a

if b < youngest:
    youngest = b
if c < youngest:
    youngest = c
if d < youngest:
    youngest = d

print("The youngest age is:", youngest)


# In[2]:


#question 4
salary = float(input("Enter your salary: "))
years = int(input("Enter years of service: "))

if years > 10:
    bonus = 0.10 * salary
elif years >= 6:
    bonus = 0.08 * salary
else:
    bonus = 0.05 * salary

print("Bonus amount: Rs", bonus)


# In[3]:


#question 6
price = float(input("Enter marked price: "))

if price > 10000:
    discount = 0.20 * price
elif price > 7000:
    discount = 0.15 * price
else:
    discount = 0.10 * price

net_price = price - discount
print("Net price after discount: Rs", net_price)


# In[4]:


#question7
eng = int(input("Enter English marks: "))
math = int(input("Enter Math marks: "))
sci = int(input("Enter Science marks: "))
sst = int(input("Enter Social Studies marks: "))

if eng > 80 and math > 80 and sci > 80 and sst > 80:
    print("Stream: Science")
elif eng > 80 and math > 50 and sci > 50:
    print("Stream: Commerce")
elif eng > 80 and sst > 80:
    print("Stream: Humanities")
else:
    print("No specific stream allotted")


# In[6]:


#question 8
num = int(input("Enter a number: "))

if num % 5 == 0:
    print("Hello")
else:
    print("Bye")


# In[8]:


#question 10
num = int(input("Enter a number: "))

if num >= 100 and num <= 999:
    print("It's a three-digit number")
else:
    print("It's not a three-digit number")


# In[ ]:




