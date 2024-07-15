# dictionary. associating something with something

students = {
    "Hermoine": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin"
    }

#Manually printing the values of the keys
print(students["Hermoine"])
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])

# when we use the for loop in dictionary we get the keys
for student in students:
    print(student)

# to get the value we need to iterate with the key itself
for student in students:
    print(student, students[student], sep=", ")