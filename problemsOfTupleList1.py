
#Wap to check if a list has palindromes in it.
list=[1,2,2,1] #original
list3=[1,2,3,1]
list1=list.copy()
list1.reverse() #reversed and copied
if(list==list1):
    print("they are palindromes")
else:
    print("They are not palindromes")
list2=list3.copy()
list2.reverse()
if(list2==list3):
    print("they are palindromes")
else:
    print("They are not palindromes")
