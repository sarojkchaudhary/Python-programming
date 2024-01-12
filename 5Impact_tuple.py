#Tuple
# t=()
# print(type(t))
# s=tuple()
# print(type(s))
#--------------------
#Decimal too binary
n=int(input())
l=[]
while(n):
    a=n%2
    l.append(a)
    n=n//2
l=l[::-1]
for i in l:
    print(i,end="")

    
