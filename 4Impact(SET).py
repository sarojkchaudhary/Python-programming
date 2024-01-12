# count repeated values 

# n=input()
# r=set(n)
# l=list(r)
# l.sort()
# print(l)
# for i in l:
#     print(i,"=",n.count(i))

#aabccde----->a2b1c2d1e1


# n=input()
# r=set(n)
# l=list(r)
# l.sort()
# print(l)
# s=''
# for i in l:
#     s=s+i,str(n.count(i))
# print(s)

#----------------------------
# n=input()
# r=set(n)
# l=list(r)
# l.sort()
# print(l)
# for p in l:
#     if (n.count(p)>1):
#         print(p,"-",str(n.count(p)),end=(" "))
#----------------
# n=int(input())
# s=set()
# for i in range(n):
#     a=int(input())
#     s.add(a)
# print(s)
#-------------------------------------------
# n=int(input())
# s=list(map(int,input().split()))[:n]
# n=int(input())
# t=list(map(int,input().split()))[:n]
# s1=set(s)
# s2=set(t)
# print(s1)
# print(s2)
# s3=s1^s2
# for i in s3:
#     print(i)

#----------------------------------------
#pending
# n=int(input())
# s=list(map(int,input().split()))[:n]
# n=int(input())
# t=list(map(int,input().split()))[:n]

# a=input()
# b=input()
# s1=set(a)
# s2=set(b)
# d=s1&s2
# l=list(d)
# l.sort()
# print(''.join(l))










