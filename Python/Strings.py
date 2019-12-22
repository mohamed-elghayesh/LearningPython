my_string="Hello my name is khaled and i am 26 years old"
print(my_string)
print(my_string.split())
print(my_string.split()[4])
print(len(my_string.split()))

print(len(my_string))
print([*my_string])


# Python program to convert a list to string   
# Function to convert   
def listToString(my_list):     
    # initialize an empty string 
    str1 = ""      
    # traverse in the string   
    for ele in my_list:  
        str1 += ele   
    # return string   
    return str1        
# Driver code     
s = ['Good', 'for', 'Thinking'] 
print(listToString(s))  
