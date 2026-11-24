l = list("abc")
t = tuple([1, 2, 3])
d = dict(name="Rahul", age=20)

print("list()  :", l)
print("tuple() :", t)
print("dict()  :", d)

# Converting between types
print(list((10, 20, 30)))
print(tuple("xyz"))
print(dict([("a", 1), ("b", 2)]))