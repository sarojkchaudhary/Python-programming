# # # # # # # # # # # # import string

# # # # # # # # # # # # alphabet = string.ascii_lowercase
# # # # # # # # # # # # print(alphabet)
# # # # # # # # # # # # import string

# # # # # # # # # # # # alphabet1 = string.ascii_lowercase
# # # # # # # # # # # # alphabet2= string.ascii_uppercase
# # # # # # # # # # # # print(alphabet1)

# # # # # # # # # # # #----------------------------------------------
# # # # # # # # # # # # s=input()
# # # # # # # # # # # # s=s.lower()
# # # # # # # # # # # # r=''
# # # # # # # # # # # # for i in range(97,123):
# # # # # # # # # # # #     d=chr(i)
# # # # # # # # # # # #     if d not in s: 
# # # # # # # # # # # #         r=r+d
# # # # # # # # # # # # print(r)



# # # # # # # # # # # li=list(map(str,input().split(" ")))
# # # # # # # # # # # for i in li:
# # # # # # # # # # #     j=i[::-1]
# # # # # # # # # # #     print(j,end=" ")
 

# # # # # # # # # # n=input()
# # # # # # # # # # s=n.split()
# # # # # # # # # # for i in s:
# # # # # # # # # #     j=i[::-1]
# # # # # # # # # #     print(j,end=" ")

# # # # # # # # # #wap to print prme between 1 to 5

# # # # # # # # # for i in range(2,51):
# # # # # # # # #     c=0
# # # # # # # # #     for j in range(1,i+1):
# # # # # # # # #         if(i%j==0):
# # # # # # # # #             c=c+1
# # # # # # # # #     if(c==2):
# # # # # # # # #         print(i,end=" ")


# # # # # # # # #print perfect number from 1-100
# # # # # # # # #6--->1,2,3----->20----->1,2,3,4,7,14

# # # # # # # # # for p in range(1,101):
# # # # # # # # #     s=0
# # # # # # # # #     for q in range (1,p//2+1):
# # # # # # # # #         if(p%q==0):
# # # # # # # # #             s=s+q
# # # # # # # # #     if(s==p):
# # # # # # # # #             print(p,end=" ")

# # # # # # # # s=input()
# # # # # # # # r=''
# # # # # # # # for p in s:
# # # # # # # #     d=int(i)
# # # # # # # #     if(d%2!=0):
# # # # # # # #         v=d*d
# # # # # # # #         r=r+str(v)
# # # # # # # # print(r)
        



# # # # # # # n=input()
# # # # # # # c=len(n)
# # # # # # # for n in range(c+1):
# # # # # # #     if n%2!=0:
# # # # # # #         print(n*n,end='')



# # # # # # i=1
# # # # # # while(i<=10):
# # # # # #     print(i,end=" ")
# # # # # #     i=i+1
# # # # # # i=1
# # # # # # while(i<=10):
# # # # # #     if (i%2==0):
# # # # # #             print(i,end=" ")
# # # # # #     i=i+1


# # # # # # i=1
# # # # # # while(i<=10):
# # # # # #     if (i%2!=0):
# # # # # #             print(i,end=" ")
# # # # # #     i=i+1






# # # # # #Write a program sum of digit  
# # # # # n=int(input("Enter the number: "))
# # # # # s=0
# # # # # while (n!=0):
# # # # #     r=n%10
# # # # #     s=s+r
# # # # #     n=n//10
# # # # # print("sum: ",s)


# # # # #check 123 is palidrome or not


# # # # num = int(input("Enter a number: "))

# # # # str = str(num)
# # # # if str == str[::-1]:
# # # #     print(" palindrome.")

# # # # else:
# # # #     print("Not palindrome.")


# # # n=int(input("Enter n:"))
# # # s=0
# # # m=n
# # # while(n!=0):
# # #     r=n%10
# # #     s=(s*10)+r
# # #     n=n//10
# # # print("Reverse: ",s)
# # # if(s==m):
# # #     print("palindrome")
# # # else:
# # #     print("Not palindrome: ")




# # #89-------->Disarium number
# # 9^2+8^1=81+8=89
# # 175----> 

# n=int(input())
# l=len(str(n))
# s=0
# m=NameError
# while(n!=0):
#     r=n%10
#     s=s+(r**l)
#     n=int(n/10)
#     l=l-1
# if(m==s):
#     print("Disarium")
# else:
#     print("NOt Disarium")








