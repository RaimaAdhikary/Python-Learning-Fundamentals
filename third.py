#ternary operator
salary=float(input("Salary is: "))
tax=(salary*0.1,salary*0.2)[salary>=50000]
print(tax)

#simple ternary
food=input("Food is")
eat= True if food =="cake" else False
print(eat)