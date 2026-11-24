name = "Anita"
age = 21
marks = 87.5

print("Name:", name, "Age:", age, "Marks:", marks)
print("Name: {}, Age: {}, Marks: {}".format(name, age, marks))
print(f"Name: {name}, Age: {age}, Marks: {marks:.2f}")
print("Name: %s, Age: %d, Marks: %.1f" % (name, age, marks))
print(name, age, marks, sep=" | ", end="!\n")