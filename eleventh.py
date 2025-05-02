#nesting
#WAP to find whether your inputted age is suitable to drink wine
age=int(input("enter your age: "))
if(age>=18):
    if(age>=80):
        print("Cannot Drink alcohol")
    else:
        print("Can Drink Alcohol")
else:
    print("Cannot Drink Alcohol")

#WAP to find whether the input is odd or even
inp=int(input("Enter the number"))
if(inp%2==0):
    print("The number is even")
else:
    print("The number is odd")

#WAP to find the greatest of three numbers entered by the user

a=int(input("Enter First: "))
b=int(input("Enter second: "))
c=int(input("Enter third: "))
if(a>b):
    if(a>c):
        print(a," is largest.")
    elif(a<c):
        print(c ,"is largest")
elif(a<b):
    if(b>c):
        print(b, "is largest")
    else:
        print(c, " is largest")


#WAP to check if a number is a multiple of 7 or not

d=int(input("Enter value: "))
if(d%7==0):
    print(d, "is a multiple of 7")
else:
    print(d, "is not a multiple of 7")
