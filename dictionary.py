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
