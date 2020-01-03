import os

# CWD is Atom so to read from Python subfolder
""" write_to = open("Python\\Test.txt","w")
write_to.write("Hello World\nThis is a good example\nfor learning file methods")
write_to.close()

read_file = open("Python\\Test.txt","r")
print([*read_file])
read_file.close() """

append_to = open("Python\\Test.txt","a")
append_to.write("This should go to the last line.")
print([*append_to])
append_to.close()