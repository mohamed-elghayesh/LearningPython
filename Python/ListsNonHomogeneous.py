# a list of people
people = [["Ahmed", "Ali", 25, 5600],
        ["Mona","nasser", 22, 4700],
        ["Samah","Kamal", 28, 4800],
        ["Mansour","Ramadan",42,8300],
        ["Waheed","Tolba",38,6800]]

# print(people[2])
# print(people[2][3])
# print(people[2:-1])

# lists allow indexing, concatenation (+), repetition (*),
# membership (in), length (len()), count(item), slicing ([1:]), pop(i)

# passing a list to  function
def edit_people(my_list):
        my_list[0][1]="Gamal"
        print("inside: ",my_list[0])

# Call edit_people()
edit_people(people)
print("outside: ",people[0])

# passing a list as a parameter creates a reference to the list

# unpacking
print("\nunpacking a[1,2,3,4,5,6]")
a=[1,2,3,4,5,6]
x,*y=a
print("x= ",x,"\ny= ",y)
print("a= ",a,"\n*a= ",*a)