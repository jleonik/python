text = 'Sample Text\nNew line'

#'file' is a normal variable
file = open('exampleFile.txt','w') #'w' clears everything before writing. If the file doesn't exist it will be created
file.write(text)
file.close()

appendMe = '\nNew bit of text'
file = open('exampleFile.txt','a')  #'a' will append the file
file.write(appendMe)
file.close()

#Reading a file

readMe = open('exampleFile.txt','r').read()  #'r' - read mode
print(readMe)
readMe = open('exampleFile.txt','r').readlines()  #readlines will create a python list. Each line in separate list item
print(readMe)