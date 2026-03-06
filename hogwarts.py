students = ["Hermione","Harry","Ron"]

print(students)

for student in students:
    print(student)

for i in range(len(students)):
    print(i,students[i])

#Dictionary in python
students = {
    "Hermione":"Gryffindor",
    "Harry":"Gryffindor",
    "Ron":"Gryffindor",
    "Draco":"Slytherin"
}

for student in students:
    print(student,students[student],sep=": ")