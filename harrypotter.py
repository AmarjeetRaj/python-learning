import csv
students = []

with open("harrypotter.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        name = row[0]
        home = ", ".join(row[1:])
        students.append({"name": name, "home": home})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")