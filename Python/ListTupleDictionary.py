# Mutable list of values
List1 = ['one', 2, 4.5, 'Ferrari']
List2 = ['one', 2, 4.5, 'Ferrari']
List2[2]
print(List1 == List2)
print(List1 is List2)
print("List1 id: ", id(List1))
print("List2 id: ", id(List2))
List2 = List1.append(66)
print("List2 id: ", id(List2))

# Immutable set of values
Tuple1 = ('one', 2, 4.5, 'Ferrari')
Tuple1[2]
Tuple2 = ('one', 2, 4.5, 'Ferrari')
print(Tuple1 == Tuple2)
print(Tuple1 is Tuple2)
print("Tuple1 id: ", id(Tuple1))
print("Tuple2 id: ", id(Tuple2))

# Like lists but key:value pairs
Dictionary1 = {}
Dictionary2 = {'name':'Ahmed','age':24}
Dictionary2['name']

Cars = {"Ferrari":{"cost":12000, "color":"Red"}, 
        "BMW":{"cost":10000,"color":"Grey"}}

print(Cars["BMW"])
print(Cars["BMW"]["cost"])