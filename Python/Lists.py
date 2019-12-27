# Lists: are flexible arrays that can have composite variable
# Lists are mutable, append(), extende(), del(), sort(), insert(), reverse()
a = [99, "bottles of juice", ["on","the","wall"]]
print(a[0])
print(a[1:2])
print(a[2][1])

# a list can be appended from within a loop
# this is also example of making a separate copy
b = []
for i in a:
    b.append(i)
print(b)

print(id(a))
print(id(b))

# both c[] and a[] points to the same list
c = a 
a[0]=12
print("\n",a,"\n",b,"\n",c)

a.reverse()
a.remove(a[0])
del(b[2])

print("\n",a,"\n",b,"\n",c)

# sorting a list
print()
d = [2,3,1,4,-9]
d.sort()
print(d)
d.reverse()
print(d)

d.sort()
print(d)
d.sort(reverse=True)
print(d)

# inserting an element at index
d.insert(2,25)
print(d)