names = []

# Append the name to the file
with open("names.txt") as file:
    #lines = file.readlines()
    print(file)
    for line in file:
        names.append(line.rstrip())

# Read and print all names from the file
for name in sorted(names):
    print("Hello,", name.rstrip())