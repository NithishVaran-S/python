#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1)Display “Hello World” in your output screen.

print("hello dark")


# In[2]:


#2)Get the input from the user and perform addition of two numbers

a=int(input("enter the value of A:"))
b=int(input("enter the value of B:"))
c=a+b
print(c)


# In[5]:


# 3)swap two variables without temp variable

a=int(input("enter the value of A:"))
b=int(input("enter the value of B:"))

a=a+b
b=a-b
a=a-b
print("The Swapped Value Is:\n A:{0} \n B:{1}".format(a,b))


# In[8]:


#4)convert the entered kilometres 

a=int(input("Enter the value to be Converted:"))
a=a*0.621371
print("The Converted Value is {0} Km".format(a))


# In[3]:


#5)check whether the given number is positive, negative or 0

a=int(input("Enter the value:"))

if (a<0):
    print("The number is NEGATIVE")
elif(a==0):
    print("You entered ZERO")
else:
    print("The number is POSITIVE")


# In[14]:


#6)verify that the given year is a leap year

a=int(input("Enter the year:"))
if(a%100==0):
    if(a%400==0):
        print ("The year is a LEAP YEAR")
elif (a%4==0):
    if(a%100!=0):
        print ("It is a LEAP YEAR")
else:
    print ("It is not a LEAP YEAR")


# In[55]:


#7)display the prime numbers within the given interval

a=int(input("Enter the Range:"))

print("The prime numbers are ")
for i in range (2,a):
    flag=0
    for j in range (2,i):
        if (i%j==0):
            flag=1
    if(flag==0):
        print(i)


# In[89]:


#8) display the Fibonacci sequence up to n-th term

a=int(input("The total elements"))
ans=0

array=[]
for i in range (1,a+1):
    element = int(input("Element{0}=".format(i)))
    array.append(element)
print(array)
    
for i in array:
    ans=ans+i
    
print("The Fibonacci series Answer is {0}". format(ans))


# In[3]:


#9) check if the number is an Armstrong number or not

a=int(input("Enter the number"))
b=len(str(a))
print(b)
temp=a
ans=0

while temp > 0:
    digit = temp % 10
    ans += digit ** b
    temp //= 10
    
if a==ans:
    print("It is a ARMSTRONG NUMBER")
else:
    print("It is not a ARMSTRONG NUMBER")


# In[13]:


#10) Find the Sum of natural numbers up to n-th term

a = int(input("Enter the last number:"))
ans = 0

for i in range (1,a+1):
    ans = ans + i
    
print("The Sum of Natural Numbers are:{0}".format(ans))


# In[16]:


#11) Write a function called show_stars(rows

def show_stars(a):
    for  i in range (0,a+1):
        print("*"*i)
        
a=int(input("Enter the number of rows:"))
show_stars(a)


# In[100]:


#12) Write a program to remove characters from a string
#starting from zero up to n and return a new string.

string=input("Enter the string : ")
b=input("Enter the letters to be removed:")

string1=string.replace(b,"")

print("the final string is: {0}".format(string1))


# In[43]:


#13) Iterate the list of numbers and print only those divisible by 5

list=[]
list2=[]
a=int(input("Enter the number of elements"))

for i in range (1,a+1):
    b=int(input("Number {0}:".format(i)))
    list.append(b)

print(list)

for i in list:
    if(i%5==0):
        list2.append(i)
        
print(list2)


# In[55]:


#14) Wprogram to find how many times substring “Hi” appears in the string.

word=input("Enter the Word:")
count=word.count("hi")

print(count)


# In[62]:


#15) Print the following pattern

a=int(input("Enter the End Number:"))

for i in range (1,a+1):
    print("{0} ".format(i)*i)


# In[95]:


#16) Write a program to check if the given number is a palindrome number.


a=(input("Enter the number to be checked:"))
b=a[::-1]

if a==b:
    print("Your input is a PALINDROME")
else:
    print("Your input is not a PALINDROME")


# In[78]:


#17) Python program to interchange first and last elements in a list

list=[22,33,4,55,66,77]
print("The list is {0}".format(list))

temp=list[0]
list[0]=list[5]
list[5]=temp

print("The interchanged list is {}".format(list))


# In[79]:


#18)Python program to swap two elements in a list

list=[11,22,33,44,55,]
print(list)

a=int(input("Enter the first number:"))
b=int(input("Enter the Second number:"))

list[a],list[b]=list[b],list[a]

print("The interchanged list is {}".format(list))


# In[85]:


#19)Python Ways to find length of list

list=[11,33,22,45,33]
count=0

#using len() method
a=len(list)

#using for loop method
for i in list:
    count= count+1

print("The length is",a)
print("The length is",count)


# In[91]:


#20)Maximum of two numbers in Python

a=int(input("First Number:"))
b=int(input("Second Number:"))

if a>b :
        print("First is the greatest")

else:
        print("Second is the greatest")


# In[92]:


#21)Minimum of two numbers in Python

#20)Maximum of two numbers in Python

a=int(input("First Number:"))
b=int(input("Second Number:"))

if a>b :
        print("Second is the smallest")

else:
        print("First is the smallest")


# In[97]:


#22)Python program to check whether the string is Symmetrical 

a=(input("Enter the word to be checked:"))
b=a[::-1]

if a==b:
    print("Your word is a PALINDROME")
else:
    print("Your word is not a PALINDROME")


# In[99]:


#23)Reverse words in a given String in Python

a=input("Enter the string:")

b=a[::-1]

print("The reversed string:",b)


# In[104]:


#24)Ways to remove i’th character from string in Python

a=input("Enter the word:")
b=int(input("The index to be removed:"))

c=a[:b]+a[b+1:]

print("The altered string is ",c)


# In[110]:


#25)Find length of a string in python 

a=input("Enter the string:")

b=len(a)

print("The length of the string ""{0}"" is {1}".format(a,b))


# In[123]:


#26)Python program to print even length words in a string

a=input("Enter your sentence:")
b= a.split()

print("The even words in the list is:")

for i in b:
    if len(i) %2==0:
        print(i) 
    


# In[2]:


#27)Python program to Find the size of a Tuple

tuple = (1, 2, 3, 4, 5)

len = len(tuple)

print("Size of the tuple:",len)


# In[8]:


#28)Python – Maximum and Minimum K elements in Tuple

tuple = (5, 10, 3, 8, 6, 12, 7, 1, 9, 4)

largest = sorted(tuple)[-1:]
print("Largest elements in the tuple is", largest)

smallest = sorted(tuple)[:1]
print("Smallest elements in the tuple is", smallest)


# In[11]:


#29)Python – Sum of tuple elements

tuple=(1,2,3,4,5)
ans=0

for i in tuple:
    ans = ans+i
    
print("The sum of the tuple is ",ans)


# In[12]:


#30)Input matrix as a tuple of tuples

matrix = (
            (1, 2, 3),
            (4, 5, 6),
            (7, 8, 9)
         )

row_sums = [sum(row) for row in matrix]

print("Row-wise element addition:")

for i, row_sum in enumerate(row_sums):
    print("Row", i+1, "sum:", row_sum)


# In[ ]:




