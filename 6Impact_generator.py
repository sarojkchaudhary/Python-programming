#genereator
# def gen():
#     yield 5
#     yield 10
#     yield 20
#     yield 30
#     yield 40
# g1=gen()
# r1=next(g1)
# r2=next(g1)
# r3=next(g1)
# r4=next(g1)
# r5=next(g1)
# print(r1,r2,r3,r4,r5)
#------------------------------------
# def gen():
#     l=[5,10,5,20,25]
#     for p in l:
#         yield p
# g1=gen()
# for p in g1:
#     print(p,end=" ")

#-----------------------------------
#random function
# import random
# s=random.randint(1,100)
# t=random.randint(100,1000)
# u=random.randint(1000,10000)
# v=random.randint(10000,100000)
# print(s)
# print(t)
# print(u)
# print(v)
#----------------------------------
#write a program to generate 4 random opt with in the range of 1000 to 10000
# import random
# def gen():
#     i=1
#     while(i<=10):
#         d=random.randint(1000,10000)
#         yield d
#         i=i+1
# g1=gen()
# for i in g1:
#     print(i)
    #------------------------------------
#write a program to generate factorial of the
#number of from 5 t 10 and return  the values in main program

# def fact(a,b):
#     for i in range(a,b+1):
#       f=1
#       for q in range(1,i+1):
#          f=f*q
#       yield f
# g1=fact(5,10)
# for i in g1:
#    print(i)

#--------------------------------------
# l=[1,2,3,4,5,6,7,8,9,10]
# r=iter(l)
# for i in r:
#     print(i,end=" ")
#--------------------------
# l=[1,2,3,4,5,6,8,9,10]
# e=enumerate(l)
# for i in l:
#  print(i)
#--------------------------
#clouser
# def power(p):
#     def pow(n):
#         return p**n
#     return pow
# s=power(5)
# p=s(2)
# print(p)
# s=power(4)
# p=s(3)
# print(p)
#--------------------------
#output- 
#***********
#$$$$$$$$$$$ by using clouser
# def star(a):
#     def dollar(b):
#         print (a*b)
        
#     return dollar
# s=star("*")
# s(10)
# s=star("$")
# s(10)  
#-----------------------------------------
#Decorader
# def new_diplay(d):
#     def smart_display():
#         print("******************")
#         d()
#         print("******************")
#     return smart_display
# @new_diplay
# def display():
#     print("Hello word")
# display()
#--------------------------------------------------
# def smart_div(d):
#     def division(a,b):
#         if b==0:
#             return 0
#         else:
#             return d(a,b)
#     return division
# @smart_div
# def div(a,b):
#     return a/b
# a=div(10,2)
# print(a)
# b=div(10,0)
# print(b)
#--------------------------------------------------------

#
# def smart_div(d):
#     def division(a,b):
#         if type(b) ==str:
#             return "String Cannot div int"
#         else:
#             return d(a,b)
#     return division
# @smart_div
# def div(a,b):
#     return a/b
# a=div(10,"abc")
# print(a)
# b=div(10,5)
# print(b)
#-------------------------------------------

#list comphrehension
# print([i for i in range(1,21) if i%2==0])

#write a program to read 5 values from the user using with and without list comphreshino
# l=[]
# for i in range(1,6):
#     val=int(input())
#     l.append()
# print[l]
#by using list comphrension
# l=[int(input("enter the value"))for i in range(1,6)]
# print(l)
#--------------------------------------------
#write a program to pint square of the odd number from 30 to 50
# l=[i**2 for i in range(1,10) if (i%2==1) ]
# print(l)

   #---------------------------
#write a progam to create 3*3 nested list and accesed the element present in the list 
# l=[[1,2,3],[4,5,6],[7,8,9]]
# print(l)
# for i in l:
#     print(i)
#     print("---------")
#     for q in i:
#         print(q)
    
#-----------------------------------------
#Write a program to create nested list ad read the value from the user:
# s=[]
# for i in range(3):
#     t=[]
#     for q in range(3):
#         val=int(input("Enter the value: "))
#         t.append(val)  
        
#     s.append(t) 
    
# print(s)
#----------------------------------
#find max1,and max 2
# n=int(input())
# l=list(map(int,input().split()))[:n]
# l.sort()
# print("max1:",l[-1])
# c=l.count(l[-1])
# d=l[-(c+1)]
# print("second max:",d)

#--------------------------------------
#min
# n=int(input())
# l=list(map(int,input().split()))[:n]
# l.sort()
# print("min1:",l[0])
# c=l.count(l[-1])
# d=l[1+(c-1)]
# print("second min:",d)
#=--------------------
#write a prgoram to create  nested list and read the value from the user usigg the list comprehension
# l=[[int(input("Enter the value "))for q in range(3)]for p in range(3)]
# print(l)

#-----------------------------------

#write a program to read 2*2 nested list element 
#for 2 matrixes and perform the addition operation

# l1=[[int(input("Enter the value "))for q in range(2)]for p in range(2)]
# l2=[[int(input("Enter the value "))for q in range(2)]for p in range(2)]
# c=[[0,0],[0,0]]
# for p in range(2):
#     for q in range(2):
#         c[p][q]=l1[p][q]+l2[p][q]
# for p in range(2):
#     for q in range(2):
#         print(c[p][q],end=" ")
#     print()

#=--------------------------------------------
#Write a programto read find row wise sum
# l1=[[int(input("Enter the value "))for q in range(3)]for p in range(3)]
# l2=[]
# for p in l1:
#     a=sum(p)
#     l2.append(a)
# print(l2)

#--------------------------
# l1=[[int(input("Enter the value "))for q in range(3)]for p in range(3)]
# print(l1)
# r=[]
# for p in range(3):
#     s=0
#     for q in range(3):
#         s=s+l1[p][q]
#     r.append(s)
# print(r)
#Write a program to sum of colum element
# l1=[[int(input("Enter the value "))for q in range(3)]for p in range(3)]
# print(l1)
# r=[]
# for p in range(3):
#     s=0
#     for q in range(3):
#         s=s+l1[q][p]
#     r.append(s)
# print(r)

#---------------------------------------
#Exception handling
# print("Begin")
# a=int(input("a: "))
# try:
#     b=int(input("b: "))
#     c=a/b
#     print(c)
# except(ZeroDivisionError):
#     print("Second no can't be zero!")
# print("end")
#------------------------------------------------












