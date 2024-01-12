# s={"Name":"Saroj kumar","id1":5233,"Dept":"CSE","Salary":100000}
# print(s)
# print(s["id1"])
# for p in s.keys():
#     print(p)
# for p in s.values():
#     print(p)
# for p,q in s.items():
#     print(p,q)
# for p in s.items():
#     print(s)

# for p in s.items():
#     print(p[0],p[1])


# d={"Name":"Saroj","Inrollment":"210306105233","Div":"6A1","Courses":"B.tech"}
# for p in d.items():
#     print(p)


#wap to print square of the even number from 1 to 20
# key= number, values is the square

# d={p:p*p for p in range(1,21) if (p%2==0)}
# print(d.values())

#Write a program to print cubes of the odd number from 30 to 50


# d={p:p**3 for p in range(30,51) if (p%2!=0)}
# print(d.values())

#---------------------------------
# x="Parul University"
# d={p:x.count(p)  for p in  x}
# print(d)


#write a program read string form the user and print vowel character count

# s=input()
# d={p:s.count(p) for p in s if p in "a,e,i,o,u" }
# print(d)


# s=input()
# d={p:s.count(p) for p in s if p in "aeiou" }
# m=max(d.values())
# for p,q in d.items():
#     if(q==m):
#         print(p)
# print(m)
# s=input()
# x=input()
# d={p:s.count(p) for p in s if p in s}
# m=max(d.values())
# l=[]
# for p,q in d.items():
#     if(m==q):
#         l.append(p)
# l.sort()
# res=''
# for p in s:
#     if(p==l[0]):
#         res=res+x

#     else:
#         res=res+p

# print(res)

#---------------------------
# n=int(input())
# l=list(map(int,input().split()))[:n]
# li=[]
# m={p:l.count(p) for p in l}
# for p,q in m.items():
#     if(p==q):
#         li.append(p)
# if(len(li)>=1):
#     print(max(li))
# else:
#     print("-1")


# d={"raju":45,"anil":56,"zoo":34,"Sarita":2,"bharathi":29,"krishna":32}
# r=sorted(d.keys())
# e={}
# print(r)
# for s in r:
#     for p,q in d.items():
#         if (s==p):
#              e.update({p:q})
#              break  
# print(e)  
#     d={"raju":45,"anil":56,"zoo":34,"Sarita":2,"bharathi":29,"krishna":32}
# r=list(d.keys())
# r.sort()
# e={}
# print(r)
# for s in r:
#     for p,q in d.items():
#         if (s==p):
#              e.update({p:q})
#              break  
# print(e)

# d={"krishna":[23,21,24],"raju":[21,20,18],"Sarita":[22,20,16]}
# for p,q in d.items():
#     print(p)
#     s=sum(q)
#     avg=s/len(q)
#     print("Avg:%.2f"%avg)
   #Hacker Rank Question
# Taking input from the user to create a dictionary


# n = int(input())
# d={}
# for p in range(n):
#     name,*m=input().split()
#     marks=list(map(int,m))
#     d.update({name:marks})
# print(d)
# name=input()
# m1=d[name]
# avg=sum(m1)/len(m1)
# print("Avg:%.2f"%avg)


#-----------------------------------------
# Write a  program to read string from the user and find reverse of a string check wether it is palindrome or not


# s=input()
# r=""
# for p in range(len(s)-1,-1,-1):
#     r=r+s[p]
# print(r)
# if r==s:
#     print("yes")
# else:
#     print("no")

#-------------------------
#count vowel and consonant
# s=input()
# v=0
# c=0
# for i in s:
#     if i=="aeiou":
#         v=v+1
        
#     elif i==" ":
#         pass
#     else:
#         c=c+1
# print(v)
# print(c)


#-----------------------------
n=int(input())
s=list(map(str,input().split()))
d={}
for p in s:
    if s.count(p)>=n:
        q=s.count(p)
        d._setitem_(p,q)
           
print(*d.keys())












































   






