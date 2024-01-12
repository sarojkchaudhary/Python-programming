#Function without argument & without return type
# def even_odd():
    
#     n=int(input())
#     if(n%2==0):
#        print(n,"Even number")
#     else:
#         print(n,"Odd number:")
# even_odd()
# d=even_odd
# d()
#--------------------------------------
#With argument & without return type

# def even_odd(n):
#     if(n%2==0):
#        print(n,"Even number")
#     else:
#         print(n,"Odd number:")
# n=int(input())
# even_odd(n)
#------------------------------------
#With Argument & With return Type
# def even_odd(n):
#     if(n%2==0):
#        return 1
#     else:
#         return 0
# n=int(input())
# s=even_odd(n)
# if(s==1):
#     print(n," is Even Number")
# else:
#      print(n,"is odd number")
#----------------------------------------
# def weight(i):
#     w=10**(ord(i)-ord("A"))
#     return w
# d=int(input())
# s=0
# for i in d:
#     r=weight(i)
#     s=s+r
# print(s)
#---------------------------------
#Palindrome or not
# def palindrome(l):
#     f=0
#     for p in l:
#         d=str(p)
#         if(d!=d[::-1]):
#             f=0
#             break
#         else:
#             f=1
#         if(f==1):
#             return 1
#         else:
#             return 0
# n=int(input())
# l=list(map(int,input().split()))[:n]
# s=palindrome(l)
# if(s==1):
#     print("yes")
# else:
#     print("NO")
#------------------------------------------------
#
#Lamda Fucntion
# def sum(a,b):
#     c=a+b
#     return c
# c=sum(10,15)
# print(c)
# #
# c=lambda g,h:g+h
# r=c(10,15)
# print(c)


# #Even number
# s=lambda x:x%2==0
# l=[1,2,3,4,5,6]
# r=[p for p in l if (s(p))]
# print(r)
#odd number(30,50)

# s=lambda x:x%2!=0
# r=[p for p in range(30,51) if (s(p))]
# print(r)
    
#factorail of num 5 to 10
# import math
# s=lambda x:math.factorial(x)
# r=[s(p) for p in range(5,11)]
# print(r)
#----------------------------
#write a program to perfrom add,sub,mul,div usng single function and lambda
# def op(a,b,s):
#      r=s(a,b)
    
#      return r
# s1=op(10,5,lambda a,b:a+b)
# s2=op(10,5,lambda a,b:a-b)
# s3=op(10,5,lambda a,b:a*b)
# s4=op(10,5,lambda a,b:a//b)
# print(s1,s2,s3,s4)
# l=lambda a,b:[a+b,a-b,a*b,a/b]
# w,x,y,z=l(10,5)
# print(w,x,y,z)

#--------------------------------
#MAp & FILTER
#with filter and without lambda
# def even(n):
#     return n%2==0
# l=list(range(10,31))
# r=list(filter(even,l))
# print(r)
#with lambda and filter
# l=list(range(10,31))
# r=list(filter(lambda x:x%2==0,l))
# print(r)

#---------------------------
#filter positive number without lambda

# def positive(n):
#     return n>=0
# l=list(range(-6,7))
# r=list(filter(positive,l))
# print(r)

#filter negative number with lambda

# l=list(range(-6,7))
# r=list(filter(lambda x:x<0,l))
#


#print(r)
#____________________
#upper case find with filter
# l=["acbc","ABC","xyz","WRT"]
# r=list(filter(lambda x:x.isupper(),l))

# print(r)

#MAP
# def sq(n):
#     return n*n
# a=[1,2,3,4,5,6]
# n=list(map(sq,a))
# print(n)

# l=[1,2,3,4,5]
# r=tuple(map(lambda x:x*x,l))
# print(r)
#convert to upper case with lambda,map
# s=["abc","xyz","qrt"]
# r=list(map(lambda x:x.upper(),s))
# print(r)



# print(r:=list(map(lambda x:x.upper(),["abc","xyz","qrt"])))


#reduce
#functools
# from functools import reduce
# s=[1,2,3,4,5,6]
# r=reduce(lambda a,b:a+b,s)
# print(r)
#----------------------
# from functools import reduce
# s=[1,2,3,4,5,6]
# r=reduce(lambda a,b:a*b,s)
# print(r)


#-------------------------------
#find min max
# from functools import reduce
# s=[1,2,3,4,5,6,7,8,9,10]
# r=reduce(lambda a,b:min(a,b),s)
# p=reduce(lambda a,b:max(a,b),s)
# print(r)
# print(p)
# d=[1,2,3,4,56,78,9,10]
# from functools import reduce
# m1=reduce(lambda a,b:a if a>b else b,d)
# m2=reduce(lambda a,b:a if a<b else b,d)
# print(m1)
# print(m2)



