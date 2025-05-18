info={
    "name":"Samiha",
    "Roll":1976,
    "age":15,
    "marks":[20,15,18],
    "City":"Rajshahi"
}
print(info)
print(type(info))
info["name"]="Anamika"
print(info)
null_info={

}
print(null_info)

print(type(null_info))
#making an empty dictionary into nested dictionary
null_info["Name"]="Pyramid"
null_info["Subjects"]={}
null_info["Subjects"]["Physics"]=56
null_info["Subjects"]["Chemistry"]=80
null_info["Subjects"]["Math"]=84
print(null_info)
print(null_info["Subjects"])
print(type(null_info["Subjects"]))
print(null_info.keys()) # keys is a method and it doesnot fetch inner dicts
print(info.keys())
print(len(info))
print(len(info.keys()))
print(info.values())## values is a method and it returns only the values
#type casting changing the dictionary into a list

print(list(info.values()))

print(info.items())
print(list(info.items()))
pairs=list(info.items())
print(pairs[0],pairs[1])
#get("Key") doesnot disrupt the whole code since it returns something nonetheless
print(info["City"])
#print(info["City2"]) cause an error
print(info.get("City"))
print(info.get("City2"))

#update() 

new_dict={
    "City":"Wisconsin",#overwrite
    "Zipcode":5679,
    "Country":"Madison"
}
info.update(new_dict)
print(info)
