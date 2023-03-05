#!/usr/bin/env python
# coding: utf-8

# In[ ]:


################### welcome to my python class ##################################


# What is python and why it is so popular ?
# Python is one among the most popular dynamic programming languages that is being used today. Python is an open-source and object-oriented programming language developed by Dutchman Guido van Possum in 1980s. This language can be utilized for a wide range of applications like scripting, developing and testing. Due to its elegance and simplicity, top technology organizations like Dropbox, Google, Quora, Mozilla, Hewlett-Packard, Qualcomm, IBM, and Cisco have implemented Python.
# 
# image.png
# 
# Several websites state that Python is one among the most famous programming language of 2016. Because of its implementation and syntax, it pressures more on code readability. When compared to other programming languages like C++ and Java, it requires the programmer to develop lesser codes. It offers automatic memory management and several standard libraries for the programmer. Once a programmer completes Python certification training, he can gain knowledge and experience in a wide range of top IT organizations. It is a general-purpose and high-level coding language.
# 
# Because of its features, a large number of programmers across the world, showing interest in making use of this language to develop websites, GUI applications, and mobile applications. The main reason that brings Python one among the top coding languages is that it allows the developers to figure out the concepts by developing readable and less code. Several advantages of Python supports the programmers to alleviate the effort as well as the time required for developing complex and large applications.

# In[ ]:


print("hello world")


# In[ ]:


type("hellow world")


# In[ ]:


print('hello world')


# In[ ]:


print(hello world)


# In[ ]:


type('a')


# In[ ]:


a = 5


# In[ ]:


type(a)


# In[ ]:


range(10)


# In[ ]:


type(a==5)


# In[ ]:


range(10)


# In[ ]:


list(range(10))


# In[ ]:


list(range(3,10)) ## list number from 3-9


# In[ ]:


list(range(3,10,2)) ## list  numbers from 3-9 by skipping 1 numbers in between


# In[ ]:


list(range(10,3)) ## it gives an empty list


# In[ ]:


list(range(3,10,-1))


# In[ ]:


list(range(3,10.5))


# In[ ]:


list(range(3.5,10.5))


# In[ ]:


list(range(-10,-3))


# In[ ]:


type(3.567894)


# In[ ]:


list(range(10,3,-2))


# In[ ]:


list(range(10,3,-1))


# In[ ]:


list(range(10,3))


# In[ ]:


"anand"+"rajesh"


# In[ ]:


a = input("enter a number")


# In[ ]:


a


# In[ ]:


type(a)


# In[1]:


num1 = input("enter 1st number ")
num2 = input("enter 2nd number ")

sum = num1 + num2
print(sum)


# In[3]:


num1 = float(input("enter 1st number "))
num2 = float(input("enter 2nd number "))

sum = num1 + num2
print(sum)


# In[8]:


type(sum)


# In[4]:


print("sum")


# In[5]:


print(sum)


# In[6]:


sum


# In[7]:


## design a basic cvalculator by inputiing numbers from user


# In[12]:


num1 = float(input("enter 1st number "))
num2 = float(input("enter 2nd number "))

sum = num1 + num2
diff = num1 - num2
mult = num1 * num2
div = num1 / num2
mod = num1 % num2
flr = num1//num2
pwr = num1**num2

print(sum)
print(diff)
print(mult)
print(div)
print(mod)
print(flr)
print(pwr)


# In[13]:


a = 2
a ** 2


# In[14]:


pow(3,5)


# In[15]:


pow("anand",3)


# In[20]:


"anand " *3


# In[21]:


list("anand")


# In[41]:


a = list('INDEPENDENCE')


# In[42]:


a ## or print(a)


# In[26]:


len(a)


# In[27]:


a[5]


# In[28]:


a[11]


# In[29]:


a[-2]


# In[30]:


a[::2]


# In[31]:


a[1:12:1]


# In[32]:


a[::2]


# In[34]:


a[0:11:3]


# In[36]:


a[-10:-1:2]


# In[37]:


a[::-1]


# In[38]:


a


# In[39]:


a = a[::-1]


# In[40]:


a


# In[43]:


b = a[::-1]


# In[44]:


b


# In[45]:


a = "hello how are you Ramya"
b = a[::-1]


# In[46]:


b


# In[47]:


a = "Swastik"


# In[49]:


a[3]


# In[52]:


type(a)


# In[50]:


len(a)


# In[51]:


a[3] = 'm'


# In[53]:


str_to_list = list(a)


# In[54]:


str_to_list


# In[55]:


str_to_list[3] = 'm'


# In[56]:


str_to_list


# In[59]:


empty_list = [] # create an empty list


# In[60]:


empty_list


# In[61]:


list_object = ["Seshadri",23.56,45,'m','Aakash',45,'Aakash']


# In[62]:


list_object


# In[63]:


list_object = ["Seshadri",23.56,45,'m','Aakash',45,'Aakash',['Gautam','Anand','Anil']]


# In[64]:


list_object


# In[65]:


list_object[-1]


# In[66]:


list_object[-1][1]


# In[67]:


list_object[-1][-1]


# In[68]:


list_object[-1][2]


# In[69]:


list_object.append("Ramya")


# In[70]:


list_object


# In[72]:


list_object.insert(3,"MEENU")


# In[73]:


list_object


# In[74]:


### TASK FOR YOU ALL
## LIST = [2,3,4,5,6,7,8,9,123,13,14,15,16]
## I WANT ALL MY EVEN NUMBER IN ONE LIST AND ALL MY ODD NUMBER IN ANOTHER LIST


# In[94]:


num_list = [2,3,4,5,6,7,8,9,123,13,14,15,16]


# In[95]:


num_list


# In[96]:


type(num_list)


# In[97]:


a = []
b = []


# In[98]:


len(num_list)


# In[99]:


for i in range(len(num_list)):
    if (num_list[i] % 2 == 0):
        a.append(num_list[i])
    else:
        b.append(num_list[i])


# In[100]:


a,b


# In[101]:


c = []
d = []


# In[102]:


for i in num_list:
    if (i % 2 == 0):
        c.append(i)
    else:
        d.append(i)


# In[104]:


c


# In[105]:


d


# In[106]:


'a' in "anand"


# In[107]:


list_object


# In[108]:


'Aakash' in list_object


# In[109]:


str_obj = "aesbhfwkqfhwjflKDFQWLjrpkil2wnnhlkiwfkqhrpi23ho"


# In[110]:


str_obj.find('w') ## index of the first occurrence 


# In[117]:


str_obj.find('45') ## if it doesnt exist it returns -1


# In[114]:


e = str_obj.split('j')


# In[115]:


e


# In[116]:


e[-1]


# In[113]:


str_obj.partition('j')


# In[118]:


text = "INDIA IS MY COUNTRY"


# In[123]:


text.center(50,'*')


# In[124]:


text[::-1]


# In[125]:


text


# In[127]:


s = [1,3,4,5,5]


# In[128]:


s.append([3,4,5,6,7]) ## appending a list inside a list


# In[129]:


s


# In[130]:


s.append(['Kumar',53,'Hello'])


# In[131]:


s


# In[132]:


s.extend([6,7,8,9,'Ramya']) ##wraps up the data and then insert it


# In[133]:


s


# In[134]:


var = input('Please input your name')


# In[135]:


'My name is {}'.format(var)


# In[138]:


print("My name is ", var)


# In[139]:


list(34)


# In[140]:


a = [1,2,3,4,5,6,7,8]
b = ["Anand","Manisha","Ramya","Anil"]
c = [23.45,45,67,89,30]

d = [a,b,c]


# In[141]:


d


# In[142]:


d[1][-2]


# In[143]:


d[2][1]


# In[144]:


list_num = [24,45,67,32,67,90]


# In[147]:


[i * 2 for i in list_num]


# In[ ]:




