# # # l=l=[1,4,"Krshna","Saroj","Ramu",9,7,2,0,"Apple"]
# # # s1=[]
# # # s2=[]
# # # for i in l:
# # #     if(type(i)==int):
# # #         s1.append(i)
# # #     else:
# # #         s2.append(i)
        

# # # s1.sort()
# # # s2.sort()
# # # print(s1+s2)




# # #Write a program to read list element from the user with and without using for loop:
# # # l=list(map(int,input().split()))
# # # print(l)
# # # n=int(input())
# # # l1=list(map(int,input().split()))[:n]
# # # print(l1)

# # # n=int(input())
# # # s=[]
# # # for i in range(n):
# # #     val=int(input())
# # #     s.append(val)
# # # print(s)

# # #--------------------------
# # # Wap to print first min and first largest elee
# # # n=int(input())
# # # l=list(map(int,input().split()))[:n]
# # # l.sort()
# # # r=[]
# # # for i in range(len(l)//2):
# # #     r.append(l[i])
# # #     r.append(l[-(i+1)])
# # # if (len(l)%2 !=0):
# # #     r.append(l[len(l)//2])

# # # print(*r)

# # #-----------------------------------

# # #wap to remove duplicate value of the list
# # # n=int(input())
# # # l=list(map(int,input().split())) [:n]
# # # s=[]
# # # for i in l:
# # #     if(i not in s):
# # #       s.append(i)
# # # print(s)
# # #--------------------------------------------
# # #Hacker Rank Question

# # # n=int(input("Enter Number of Operation: "))
# # # i=1
# # # l=[]
# # # while(i<=n):
# # #     cmd=input("Enter Operation: ")
# # #     s=cmd.split()
# # #     if(s[0]=="append"):
# # #         b=int(s[1])
# # #         l.append(b)

# # #     elif(s[0]=="insert"):
# # #         b=int(s[1])
# # #         c=int(s[2])
# # #         l.insert(b,c)

# # #     elif(s[0]=="remove"):
# # #         b=int(s[1])
# # #         l.remove(b)

# # #     elif(s[0]=="sort"):
# # #         l.sort(b)

# # #     elif(s[0]=="pop"):
# # #         l.pop(b)

# # #     elif(s[0]=="reverse"):
# # #         l.reverse()
    
# # #     elif(s[0]=="print"):
# # #         print(l)
# # #     i=i+1
# # #---------------------------------

# # # n=input("Enter the mobile number:")
# # # l=list(map(int,str (n)))
# # # s=[]
# # # t=[]
# # # for i in l:
# # #     if i%2==0:
# # #         s.append(i)
       
# # #     else:
# # #         t.append(i)

# # # print(*s,end=' ')
# # # print(*t)
# # #--------------------------------------------------
# # #Same question another method

# # # n=input()
# # # l=list(map(int,str (n)))
# # # a=[]
# # # b=[]
# # # for i in l:
# # #     if (i%2==0):
# # #         a.append(i)

# # #     else:
# # #         b.append(i)

# # # a.sort()
# # # b.sort()
# # # c=a+b
# # # r=list(map(str,c))
# # # print(''.join(r))

# # #----------------------------
# # #convert list number into String
# # # l=[1,2,3,4]
# # # b=[2,4,6,8]
# # # c=l+b
# # # r=list(map(str,c))
# # # print(''.join(r))

# # #-----------------------------------
# # #fibonacci series of a n number:: 

# # # n = int(input("Enter the number: "))

# # # f = [0, 1]
# # # while len(f) < n:
# # #     f.append(f[-1] + f[-2])

# # # print("Fibonacci Series:")
# # # print(f[:n])
# # # r=list(map(str,f))
# # # print(''.join(r))

# # # #---------------------------------------------

# # s=input()
# # l=len(s)
# # a=1
# # b=0
# # i=1
# # r=[]
# # while(1<=l):
# #     c=a+b
# #     r.append(c)
# #     a=b
# #     b=c
# #     i=i+1
# # res=''

# # d=str(sum(r))
# # res=res+d
# # for p in range(len(s)):
# #     res=res+s[p]+str(r[p])

# # print(res)

# #---------------------------------------
#print not repeated value 3
#
# n=list(map(int,input().split()))
# l=[]
# for i in range(len(n)):
#     if (i is in n)

# n=int(input())
# j=[]
# result_list=[]
# count=0
# for i in range(n):
#     m=input()
#     l=list(map(str,str(m)))
#     j.extend([l])
# for p in j:
#     if len(m)==15:
#         mobilenum="".join(p[0:10])
#         gen=''.join(p[11:12])
#         age=''.join(p[12:14])
#         seatno=''.join(p[14:])
#         result=[mobilenum,gen,age,seatno]
#         result_list.extend([result])
# for b in result_list:
#     if int(b[2])>=60:
#         count=count+1
# print(count)
#--------------------------------------
# wap to find count of repeated num and remove it
# l=list(map(int,input().split()))
# d=int(input())
# c=l.count(d)
# for p in range(c):
#     l.remove(d)
# print(l)
#----------------------
# n=int(input())
# l=[]
# for p in range(n):
#     val=input()
#     l.append(val)
# c=0
# for p in l:
#     d=p[11:13]
#     age=int(d)
#     if (age>=60):
#         c=c+1
#         print(p[0:10])
# print(c)

#-------------------------------
#print right leader element 
# n=int(input())
# l=list(map(int,input().split()))
# r=[]
# for p in range(len(l)):
#     for q in range(p+1,len(l)):
#         if(l[q]>l[p]):
#             break
#     else:
#         r.append(l[p])

# if(len(r)>=1):
#     print(sum(r))
# else:
#     print("-1")
   





