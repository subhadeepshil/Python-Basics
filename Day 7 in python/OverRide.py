f= open("Day 7 in python/DEMO.txt","r+")        # open the file in read mode  r+ is for overwrite mode, it will overwrite the existing content of the file. If the file does not exist, it will create a new file.
f.write("This")                                 # write a new line to the file
print(f.read())
f.close()