#1 Text file - .txt, .csv, .log,doc, .docx
#2 Binary file - .jpg, .png, .pdf, .mp3, .mp4

#we can take any filles as input and output in python
f = open("Day 7 in python/DEMO.txt","r")         # r is for read mode 
data = f.read()                 #we can also specify the number of characters to read by passing an argument to read() method, for example: f.read(5) will read first 5 characters of the file. If we want to read the file line by line we can use readline() method, for example: f.readline() will read the first line of the file and f.readline() again will read the second line of the file and so on. We can also use readlines() method to read all lines of the file and store them in a list, for example: lines = f.readlines() will read all lines of the file and store them in a list called lines. 
                                # read the content of the file and store it in data variable
print(data)                      # print the content of the file
print (type(data))               # print the type of data variable
                      # close the file after reading



line1 = f.readline()
print(line1)                      # print the first line

line2 = f.readline()
print(line2)                      # print the second line.  #just because we are reading the file line by line using readline() method, we need to close the file and open it again to read the file from the beginning. 


#we can also append data to the file using append mode "a" instead of "r" or "w". For example: f = open("Day 7 in python/DEMO.txt","a") will open the file in append mode and we can use f.write() method to write data to the file. For example: f.write("This is a new line.") will write "This is a new line." to the file. We can also use f.writelines() method to write a list of lines to the file. For example: lines = ["Line 1\n", "Line 2\n", "Line 3\n"] f.writelines(lines) will write the lines in the list to the file.

f = open("Day 7 in python/DEMO.txt","a")         # open the file in append mode
f.write("This is a new line.\n")                 # write a new line to the
f.write("This is another new line wasdwa.\n")    #we can add more lines to the file by using f.write() method multiple times. We can also use f.writelines() method to write a list of lines to the file. For example: lines = ["Line 1\n", "Line 2\n", "Line 3\n"] f.writelines(lines) will write the lines in the list to the file.
print("Data appended to the file successfully.")  # print a message after appending data to the file

f.close()                       