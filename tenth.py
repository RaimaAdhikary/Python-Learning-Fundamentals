#Strings 
str="this is a string.\n a nextline sequence."
str1= "hello"
str2="world"
print(str)
print(str1+str2)
print(str+str1+str2)
print(len(str1))
print(str1[4])
#slicing
print(str1[1:4])# starting index: ending index where ending index is not included
print(str1[2:])
print(str1[:4])
#negative slicing 
str5="ORange"
print(str5[-5:-1])
#string manipulations
st="we are going to Cananda."
print(st.capitalize())
print(st.endswith("da"))
print(st.endswith("Ca"))

print(st.find("Can"))
print(st.replace("o","e"))
print(st.replace("we","They"))
print(st.count("a"))

#Wap to input a string and find its length
inp=input("enter string: ")
print(inp)
print(len(inp))

#WAP to find the occurance of @ in a string
inp2="rai@gmail.@com"
print(inp2.find("@"))
print(inp2.count("@"))
