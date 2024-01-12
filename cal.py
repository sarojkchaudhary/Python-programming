num1=int(input("Enter the First Number::"))
print("Choose one of the operator::")
operator=input("+,-,*,/,%  ")
num2=int(input("Enter the Second Number::"))

if operator=="+":
    print(num1+num2)
elif operator =="-":
    print(num1-num2)
elif operator=="*":
    print(num1*num2)

elif operator ==("/"):
    print(a/b)

elif operator=="%":
    print(num1%num2)

else:
    print("Invalid operator!")