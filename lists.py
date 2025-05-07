#Lists are mutable
#store heterogenous collection of elements
info=["Saima", 12,"Canada",50]
print(info)
print(len(info))
info[1]=20
print(info)
print(info[1:3]) #slicing
print(info[:3])

#
list=[10,8,2]
print(list)
list.append(5)
print(list)
list.sort()
print(list)
list.sort(reverse=True)
print(list)
list.reverse()
print(list)
list.insert(2,3)
print(list)
list.remove(8) #argument is the value itself
print(list)
list.pop() # argument is index and if missing args then LIFO
print(list)
list.pop(0)
print(list)

#string list
listS=["banana","strawberry","Apple","Avocado"]
listS.reverse()
print(listS)
print(listS.sort()) # it would print None as the function invoked doesnot return anything
print(listS)
listS.insert(4,"Orange")
print(listS)


