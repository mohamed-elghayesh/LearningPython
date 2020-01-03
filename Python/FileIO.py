# CWD is Atom so to read from Python subfolder
# Creating new file then closing
write_to = open("Python\\Test.txt","w")
write_to.write("Hello World\nThis is a good example\nfor learning file methods")
write_to.close()

# reading the file then closing
read_file = open("Python\\Test.txt","r")
print([*read_file])
read_file.close()

# appending to file then closing
append_to = open("Python\\Test.txt","a")
append_to.write("\nThis should go to the last line.")
append_to.close()

read_file = open("Python\\Test.txt","r")
print([*read_file])
read_file.close()