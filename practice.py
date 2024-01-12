n=int(input("Enter the Given Input::"))
if n %2 !=0:
    print("Odd number")
else:
    if n in range (2,6) or n>20:
        print("Odd NUmber")

    elif n in range (6,20):
         print("Even")
