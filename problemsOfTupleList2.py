#WAP to count the number of students who passed grade "A" , then store these to a list and sort them from A to D
tup=("C","D","A","A","B","B","A")
print(tup.count("A"))
list=[]
list.append(tup[0])
list.append(tup[1])
list.append(tup[2])
list.append(tup[3])
list.append(tup[4])
list.append(tup[5])
list.append(tup[6])
print(list)
list.sort()
print(list)