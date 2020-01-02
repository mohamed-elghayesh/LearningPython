myl = [1,2,3,4]

def edit_list(mylist):
    mylist[1] = 4
    print(mylist)
    return mylist

edit_list(myl)
print(myl[1])
print(myl)
print(edit_list(myl))
