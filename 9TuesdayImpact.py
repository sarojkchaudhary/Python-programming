
#wap to find factorial of a number using recursion
# def f(n):
 
#     if n==0:
#         return 1
#     else:
#         d=n*(n-1)
#     return d
# s=f(5)
# print(s)

#Find sum of 1-5 numberrs using recursion:
# def f(n):
#     if n==0:
#         return 0
#     else:
#         d=n+f(n-1)
#     return d
# s=f(5)
# print(s)

#----------------------------------------------------------
#OOPS Concept
#Object Oriented Programming
# l=input()
# for p in l:
#     if(p.count(l))==l:
#         print(p)
#         break


#--------------------------------
#non-static 
# class test:
#     def insert (self):
#         self.a=1000
#         self.b=2000
#     def display(self):
#         print(self.a,self.b)
#     def update (self):
#         self.a=self.a+10
#         self.b=self.a+20

# t1=test()
# t1.insert()
# t1.display()
# t1.update()
# t1.display()
# t2=test()
# t2.insert()
# t2.display()

#-------------------------------
# class test:
#     def insert (self,a,b):
#         self.a=a
#         self.b=b
#     def display(self):
#         print(self.a,self.b)
# t1=test()
# t1.insert(100,200)
# t1.display()
# t2=test()
# t2.insert(1000,2000)
# t2.display()

# #--------------------------------------
# class test:
#     def insert (self,a,b):
#         self.a=a
#         self.b=b
#     def display(self):
#         print(self.a,self.b)
# t1=test()
# t1.insert(100,200)
# t1.display()
# print(t1.a,t1.b)

#----------------------------------
#constructor example
# class test:
#     def __init__(self):
#         self.a=100
#         self.b=200

#     def display(self):
#         print(self.a,self.b)

# t1=test()
# t1.display()
# t2=test()
# t2.display()

#-------------------------------------

#wap to find area of the circle 

# import math
# class test:
#     def __init__(self,r):
#         self.r=r
    
#     def display(self):
#         a=math.pi*self.r*self.r
#         print("Area of circle :",a)

# t1=test(3.5)
# t1.display()
# t2=test(5.5)
# t2.display()

#-------------------
#wap to fin area of the rectangular and diplay the result

# class test:
#     def __init__(self,l,b):
#         self.l=l
#         self.b=b

#     def display(self):
#         area=self.l*self.b
#         print("Area of the Rectangular:: ",area)

# t1=test(10,20)
# t1.display()
# t2=test(10,20)
# t2.display()


# #wap to create a bankng app with static ,nonstatic and local variable,constructor
# 1.before with draw >2000 don't perform transaction
# 2.before withdraw check the balance properly check sufficient balance or not

# class cust:
#     bname="CBI"
#     def __init__(self,name,accno,add,bal):
#         self.name=name
#         self.accno=accno
#         self.add=add
#         self.bal=bal

#         def display(self):
#             print(cust.bname,self.name,self.accno,self.add,self.bal)

#         def check_bal(self):
#             print("Balance: ",self.bal)
#         def deposite(self,amt):
#             self.bal=self.bal+amt
#         def withdrawa(self,amt):
#             if(amt<self.bal):
#                 if(self.bal-amt>=2000):
#                     self.bal=self.bal-amt
#                 else:
#                     print("Maintain Minimun balance:")
#             else:
#                 print("Insufficient Balance: ")

# c1=cust("Saroj",101,"nepal",45000)
# c1.display()
# c1.check_bal()
# c1.deposite(10000)
# c1.withdraw(50000)
# c1.check_bal()



                




# Write a program to develop student class with all function used
# name,rollno,address,3 sub mark
# find result if any sub fail then result fail or pass
# if student pass calculated the grade  
# class student:
#     clz="PIT"
#     bra="CSE"
#     def __init__(self,name,roll,address,math,physic,chemistry):
#         self.name=name
#         self.roll=roll 
#         self.address=address 
#         self.math=math 
#         self.physic=physic
#         self.chemsitry=chemistry

#     def display(self):
#         print(student.clz,student.bra,self.name,self.roll,self.address,self.math,self.physic,self.chemsitry)
#     def check_mark(self,math,physic,chemsitry):
#         if (math<=40):
#              if (physic <=40):
            
#                  if (chemsitry <=40):
#                      print("pass")
#                  else:
#                   print("Fail:")
# print(type)
# print(type)
# s1=student("Saroj",101,"Nepal",45,56,56)
# s1.display()


#  Write a program to creata class wit book name auther name,number of pages,cost and library name and create tree books             
# Read  the information of the main program and asing through class
# class book:
#     lname="Parul Library"
#     def __init__(self,bname,aname,np,cost):
#         self.bname=bname
#         self.aname=aname
#         self.np=np
#         self.cost=cost
#     def display(self):
#         print(book.lname,self.bname,self.aname,self.np,self.cost)



# n=int(input("Enter the number of books: "))
# i=1
# while(i<=n):
#     bname=input("Enter the Books name: ")
#     aname=input("Enter the author name: ")
#     np=int(input("Enter the number of page: "))
#     cost=int(input("Enter the cost of the books: "))

#     b1=book(bname,aname,np,cost)
#     b1.display()

#     i=i+1
#     print("*******************************")


#---------------------------------------------------------
#Create a employee class with basic employe details like emp name, empid,address and salary create tree object 
# class employee:
#     cname="Parul University"
#     def __init__(self,ename,eadd,salary):
#         self.ename=bname
#         self.eadd=eadd
#         self.salary=salary
        
#     def display(self):
#         print(employee.cname,self.ename,self.eadd,self.salary)



# n=int(input("Enter the number of employee: "))
# i=1
# while(i<=n):
#     ename=input("Enter the2 employee name: ")
#     eadd=input("Enter the address of employee: ")
#     salary=int(input("Enter the employee salary: "))
    

#     b1=employee(ename,eadd,salary)
#     b1.display()

#     i=i+1
#     print("*******************************")

#--------------------------------------------------------
#Static method

# class test:
#     def add(a,b):
#         return a+b
#     def sub(a,b):
#         return a-b
# s=test.add(10,5)
# r=test.sub(12,7)
# print(s,r)

#find  area of the triagnele using static method

# class test:
#     def tri(b,h):
#         return 0.5*b*h
# s=test.tri(10,5)
# print(s)
#------------------------------------------------
#relation between two difeerent class
# class x:
#     a=1000
#     def __init__(self):
#         self.b=2000
#     def m1(self):
#         print("in M1")
# class y:
#     c=3000
#     def __init__(self):
#         self.d=4000
#     def m2():
#         print("In m2")
#     def display(self):
#         print(y.c)
#         print(self.d)
#         y.m2()
#         x1=x()
#         print(x1.a)
#         print(x1.b)
#         x1.m1()

# y1=y()
# y1.display() 
#-----------------------------------------------------
#wap to create two classes name employee, and test
# employed detail empname, id and salary
# update the salary in test class,then calls displaymethod
# create the object of employee class in the main program and pass the oject any method define the test class

# class employee:
   
#     def __init__(self,ename,eid,esal):
#         self.ename=ename
#         self.eid=eid
#         self.esal=esal
#     def display(self):
#             print(self.ename,self.eid,self.esal)

# class test:
#     def update(e):
#       e.display()
#       e.sal=10000
#       e.display()

# e1=employee("krishna",101,1000000)
# e1.display()

# test.update(e1)

#wap to creat two classs-- student classs, find result class find mark and update the mark 


# class student:
#     def __init__(self,name,roll,mark):
#         self.name=name 
#         self.roll=roll 
#         self.mark=mark

#     def display(self):
#         print(self.name,self.roll,self.mark)

# class find_result:

#     def mark(self):
#         for




#---------------------------------------------------------
#Imheritance


# class x:
#     a=1000
#     def __init__(self):
#         self.b=2000
#     def m1(self):
#         print("IN m1")
# class y(x):
#     c=3000
#     def _init__(self):
#         self.d=4000

#         super().__init__()
#         def m2(self):
#             print("in m2")
#         def display(self):
#             print(x.a)
#             print(self.b)
#             self.m1()
#             print(y.c)
#             self.m2()
#             print(self.d)

# y1=y()
# y1.dispay()
#---------------------------------------------------

# class x:
#     a=1000
#     def __init__(self):
#         self.b=2000
#     def m1(self):
#         print("IN m1")
# class y(x):
#     c=3000
#     def _init__(self):
#         self.d=4000

#         super().__init__()
#         def m2(self):
#             print("in m2")
    
# y1=y()
# print(y.a)
# print(y1.b)
# print(y.c)
# print(y.d)
# y1.m1
# print(y.m1)
# y1.m2
# print(y.m2)
#--------------------------------------

# class x:
#     def m1(self):
#         print("In m1")
# x1=x()
# p=x1.__str__()
# print(p)
# x1.m1()
#-------------------------------------------

# class x:
#     def m1(self):
#         print("In m1")
# class y(x):
#     def m2(self):

#         print("In m2")

# print(x.__bases__)
# print(y.__bases__)
# y1=y()
# y1.m1()
# y1.m2()
# p=y1.__hash__()
# print(p)
#------------------------------------
#Multilevel inhertance

# class person:
#     def insert (self):
#         self.name="saroj"

#         self.add="Nepal"

# class employee(person):
#     def insert1(self):
#         self.id=101
# class salaried_employee(employee):
#     def __init__(self):
#         self.salary=50000
#     def display(self):
#             self.insert()
#             self.insert1()
#             print(self.name,self.add,self.id,self.salary)
# s1=salaried_employee()
# s1.display()

#----------------------------------------------------
# Heiraracy inheritacne


# class student:
#     def insert(self):
#         self.name=input("Enter the name: ")
#         self.id1=int(input("Enter the id: "))
#         self.add=input("enter the address: ")
# class DS(student):
#     def __init__(self):
#         self.s1=int(input("Enter the sub 1: "))
#         self.s2=int(input("Enter the sub 2: "))

#     def display(self):
#         self.insert()
#         print(self.name,self.id1,self.add,self.s1,self.s2,self.s3)
# class ML(student):
#     def __init__(self):
#         self.s3=int(input("Enter the sub 1: "))
#         self.s4=int(input("Enter the sub 2: "))
#     def display(self):
#         self.insert()
#         print(self.name,self.id1,self.add,self.s3,self.s4)
# d1=DS()
# d1.display()
# m1=ML()
# m1.display()

#-----------------------------------------------------------------
#Multiple Inheritance

# class x:
#     def m1(self):
#         print("In m1 of x: ")
# class y:
#     def m1(self):
#         print("In m1 of y:")
# class z(x,y):
#         def m2(self):
#              print("In m2 of z: ")
# z1=z()
# z1.m1()
            

#------------------------------------------------------------------



# class x:
#     def m1(self):
#         print("In m1")
# class y:
#      def m2(self):
#          print("In m2")
# class z:
#     def m3(self):
#         print("In m3")
# class a(x):
#     def m4(self):

#         print("In m4")
# class b(x,a):




# y1=a()
# y1.m1()
# y1.m4()



#------------------------------------------------

# class parent:
#     def add(self,a,b):
#         print(a+b)
# class child(parent):
#     def sub(self,a,b):
#         print(a-b)
# a=int(input())
# b=int(input())
# z1=child()

# z1.add(a,b)
# z1.sub(a,b)

#--------------------------------------
#polymorphism

# class x:
#     def m1(self):
#         print("In m1 with no para")
#     def m1(self,a):
#         print("in m1 with one para")
#     def m1(self,a,b):
#         print("In m1 with two para: ")
# x1=x()
# x1.m1(10,20)
        

#----------------------------------------------
#Aribitary parameter
# def d(*a):
#     print(a)
#     print(type(a))
#     print(sum(a))
# d(10,20,30)
# d(1,2,3,4,5)


# def d(b,*a):
#     print(a)
#     print(b)
#     print(sum(a)+b)
# d(10,20,30)
#-----------------------------------------------------



# class test:
#     def op(self,d,*a):
#       if (d=="int"):
#          s1=0
#       else:
#          s1=''

#       for i in a:
#          s1=s1+i
#       print(s1)
         
# t1=test()
# t1.op("int",10,20,30)
# t1.op("str","saroj","harish","Deon")
#-------------------------------------

# class x:
#     def m1(self):
#         print("in 1 of x:")
#     def m2(self):
#         print("in m2 of x: ")
# class y(x):
#     def m2(self):
#         print("in m2 of y: ")
#     def m3(self):
#             print("in m3 of y: ")
# class z(x):
#      def m1(self):
#           print("in m1 of z: ")
#      def m4(self):
#       print("In m4 of z: ")

# y1=y()
# y1.m2()
# y1.m3()
# z1=z()
# z1.m2()
# z1.m4()

#----------------------------------------------------

#Method Overriding
# class x:
#     def m1(self):
#         print("In m1: ")
#     def __str__(self):
#         return "Python"
# x1=x()
# p=x1.__str__()
# print(p)
#------------------------------------
# class x:
#     def __init__(self,name):
#         self.name=name
#     def __str__(self):
#         return self.name
# x1=x("python")
# print(x1)
# x2=x("DSA")
# print(x2)
#-----------------------------------------
# #abstract class
# from abc import*
# class RBI (ABC):
#     def min_bal(self):
#         pass
#     def RI(self):
#         print("RI is 6.5%")
# class SBI(RBI):
#     def min_bal(self):
#         print("MIn bal is 2000")
# class HDFC(RBI):
#     def min_bal(self):
#         print("MIn bal is 0")
# class ICICI (RBI):
#     def min_bal(self):
#         print("min balance is 500")
# s=input("Enter class name")
# c=globals()[s]
# c1=c()
# c1.min_bal()
# c1.RI()
#----------------------------------------------
# Abstract class
# from abc import*
# class car (ABC):
#     def __init__(self,regno):
#         self.regno=regno
#     def opentank(self):
#         print("Fill the tank with reg no: ",self.regno)
#     def steeering(self):
#         pass
#     def breaking (self):
#        pass
# class maruthi (car):
#     def steering(self):
#         print("Manual Steering: ")
#     def breaking(self):
#        print("Hydralic Break: ")
# class santro(car):
#      def steering(self):
#         print("power steering: ")
#      def breaking(self):
#        print("gas breaking system: ")
# class Tesla(car):
#     def steering(self):
#         print("Auto pilot")
#     def breaking(self):
#         print("Auto breaking: ")
# m1=maruthi("AP1550")
# m1.opentank()
# m1.steering()
# m1.breaking()

# m2=santro("AP9999")
# m2.opentank()
# m2.steering()
# m2.breaking()

# m3=Tesla("AP*****")
# m3.opentank()
# m3.steering()
# m3.breaking()

#-------------------------------------------------------------------------------
#interface
# from abc import*
# class test(ABC):
#     def operation(self):
#         pass
# class sub1(test):
#     def operation(self,a):
#         print(a*a)
# class sub2(test):
#     def operation(self,a):
#         print(a**3)
# class sub3(test):
#     def operation(self,a,b):
#         print(a+b)
# s1=sub1()
# s1.operation(5)
# s2=sub2()
# s2.operation(5)
# s3=sub3()
# s3.operation(50,50)        
            

#--------------------------------------------------------------------------------------
# from abc import*
# class vehicle(ABC):
#     def operation(self):
#         pass
# class truck(vehicle):
#     def weel(self):
#       print("12 weel")

# class car(vehicle):
#     def weel(self):
#       print("8 weel")
# class bike(vehicle):
#     def weel(self):
#       print("2 weel")
# class bus(vehicle):
#     def weel(self):
#       print("6  weel")

# t=truck()
# t.weel()
# c=car()
# c.weel()
# b=bike()
# b.weel()
# b=bus()
# b.weel()

#--------------------------------------------------------------------
#Acccess Modifire
# Public accessmodifier
#for public variable
# class employee:
#     def __init__(self,name,id1,sal,dep):
#         self.name=name
#         self.id1=id1
#         self.sal=sal
#         self.dep=dep
# e1=employee("SAroj",123,50000,"Software Engineerig")
# print(e1.name,e1.id1,e1.sal,e1.dep)




#for public method and variable
# class employee:
#     def __init__(self,name,id1,sal,dep):
#         self.name=name
#         self.id1=id1
#         self.sal=sal
#         self.dep=dep
#     def display(self):
#         print(self.name,self.id1,self.sal,self.dep)
# e1=employee("SAroj",123,50000,"Software Engineerig")
# e1.display()
#---------------------------------------
#Protected  AccessModifier
# class employee:
#     def __init__(self,name,id1,sal,dep):
#         self._name=name
#         self._id1=id1
#         self._sal=sal
#         self._dep=dep
#     def _display(self):
#         print("Name:",self._name)
#         print("ID::",self._id1)

# class geeks(employee):
#     def __init__(self,name,id1,sal,dep):
#         super().__init__(name,id1,sal,dep)
#     def display(self):
#         self._display()
#         print("salary:",self._sal)
#         print("Department:",self._dep)

# e1=geeks("SAroj",123,50000,"Software Engineerig")
# e1.display()

#--------------------------------------------------

# class employee:
#     __ename="Praul"
#     def __init__(self,name,id1,sal,dep):
#         self.__name=name
#         self.__id1=id1
#         self.__sal=sal
#         self.__dep=dep
#     def __display(self):
#         print("Name:",self.__name)
#         print("ID:",self.__id1)
#         print("SAlary:",self.__sal)
#         print("DEpartment:",self.__dep)

#     def display(self):
#         self.__display()

# e1=employee("Saroj",101,500000,"CSE")
# e1.display()
# print("*****************************")
# print(e1._employee__name)
#----------------------------------------------------------
#wap to produce number from 5 to 1 and append to the list using recursion.
# def rec(num, li):
#     if num > 0:
#         li.append(num)
#         rec(num - 1, li)
# li= []
# rec(5,li)
# print(li)


# def rec(num, li):
#     if num > 0:
#         li.append(num)
#         rec(num + 1, li)
# li= []
# rec(5,li)
# print(li)


#write a program to print 5th table using recursion

















































        









    
        