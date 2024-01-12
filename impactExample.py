# # # # >=6000---4%
# # # # >=3000--->3%
# # # # >==2000--->2%
# # # # >=1000--->1%
# # # # <1000-->No discout, After Discount display final balance   
# # # name=input("Enter the Name:")
# # # amount=int(input("Enter the amount: "))
# # # if amount>=6000:
# # #     print((Dis==amount*0.04))
# # #     amount=amount-Dis

# # # elif amount>=3000:
# # #     print((Dis==amount*0.03))
# # #     amount
# # # elif amount>=2000:
# # #     print(amount*0.02)
# # # elif amount>=1000:
# # #     print(amount*0.01)
# # # else:
# # #     print("NO discount:")

# # # print("Final amount After Discount: ",amount)

# #-------------------------------------------------------------
# # #Write a program to read name of the student ,roll no and 3 sub mark
# # if student is pass calculated the rade of the student

# # name=input("Enter the Name of  Student: ")
# # rno=int(input("Enter the roll no: "))
# # s1,s2,s3=map(int,input("3 sub mark: ").split(","))
# # print("Name: ",name)
# # print("Roll No: ",rno)
# # print("math ",s1,"Physic",s2,"Chemistry",s3)

# # if((s1>=35) and (s2>=35)and (s3>=35)):
# #     total=s1+s2+s3
# #     avg=total/3
# #     if(avg>=60):
# #         print((name,"First Grade"))
# #     elif(avg>=50):
# #         print(name,"Second Grade")
# #     elif(avg>=35):
# #         print(name,"Third Grade")
# # else:
# #     (name,"is fail")



# # ---------------------------------------------------------------
#     #Write a program to read from user and check whether is divisible by 3 and  5 or not.

# a=int(input("Enter the number: "))
# if a%3==0:
#     if a%5==0:
#         print("a is divisible by 3 and 5 ")

#     else:
#         print("Divisible by 3 and NOt divisible by 5")

# else: 
#       

#     print("NOt divisile by both")

# if a%5==0:


#-------------------------------------------------------------------------------

   
#s="Lokesh it"
# print(s[2])
# print(s[2:5])
# print(s[::1])
# print(s[2:])
# print(s[:6])
# print(s[::1])
# print(s[::1])
# print(s[::2])
# print(s[::3])
# print(s[::2][::3])
# print(s[::2][::3][::1])
# print(s[7:3])

# s="lokesh it"
# print(s[-2])
# print(s[-5])
# print(s[-2:-5:-1])
# print(s[-2:-5])
# print(s[-2:-5:-1])
# print(s[-1:-9:-2])
# print(s[-2:-8:-3])
# print(s[::-1])
# print(s[-1:-10:-1])
# print(s[::-2])
# print(s[2:-2])
# print(s[3:-3])
# print(s[-5])
# print(s[-4:][5:])
# print(s[-6:-3][3:6])


# s="Rohith"
# r=1
# d=''
# d=s[r:]+s[:r]
# print(d)


# s=input("Enter the chr: ")
# r=int(input(":"))
# d=''
# d=s[-2:]+s[:-2]
# print(d)

n=int(input("Enter the size of the list: "))
li=list(map(int,input("Enter the list Value: ").split(",")))[:n]
r=int(input())
d=[]
d=li[-r:]+li[:-r]
print(*d)












