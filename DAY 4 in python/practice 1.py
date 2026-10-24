#Dictionary in python
#Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
#Dictionaries are written with curly brackets, and they have keys and values.

student1={"name":"Subhadeep","marks":80.5,"city":"Kolkata"}     #we can store different data types in a dictionary {}
print(student1)          #to print the dictionary


info={
    "name":"Subhadp",
    "marks":80.5,
    "age":25,
    "is adult": True,
    "subject":{"Math": 90, "Science": 85}
}
print(type(info))          #to know the type of data structure we are using "type"


info["name"]= "Subhadeep"       #we can change the value of a dictionary element by using the key
info["surname"]= "Shil"        #we can change the value of a dictionary element by using the key
print(info)




#we can also create empty dictionary and add elements to it later

null_dict={}          #to create an empty dictionary
null_dict["name"]="Subhadeep"        #to add elements to the dictionary we use the key and value
print(null_dict)




#NESTED DICTIONARY
student={
    "name":"Subhadeep",
    "marks":80.5,
    "age":25,
    "is adult": True,
    "subject":{"Math": 90, "Science": 85} #we can also store a dictionary inside another dictionary, this is called nested dictionary
}
print(student["subject"]["Math"])          #to access the value of a nested dictionary we use the key of the outer dictionary and the key of the inner dictionary