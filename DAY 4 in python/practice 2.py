#Dictionary Methods
#keys() method is used to get the keys of the dictionary
student={
    "name":"Subhadeep",
    "age":20,
    "grade":"A"
 }
print(list(student.keys()))    
print(len(list(student.keys())))      #to get the keys of the dictionary we use the keys() method



#Values() method is used to get the values of the dictionary
print(list(student.values()))
print(len(list(student.values())))     #to get the values of the dictionary we use the values() method


#items() method is used to get the key-value pairs of the dictionary
print(list(student.items()))          #to get the key-value pairs of the dictionary we use the items() method


pairs=list(student.items())          #to get the key-value pairs of the dictionary we use the items() method and store it in a variable
print(pairs[1])          #to get the value of a specific key we use the key inside the square brackets


#.get() method is used to get the value of a specific key, if the key is not present in the dictionary it returns None
print(student.get("name"))       #to get the value of a specific key we use the get() method and pass the key as an argument
print(student.get("surname"))    #if the key is not present in the dictionary it returns None

#update() method is used to update the value of a specific key, if the key is not present in the dictionary it adds the key-value pair to the dictionary
student.update({"name":"Subhadeep Shil"})     #to update the value of a specific key we use the update() method and pass the key-value pair as an argument
print(student)