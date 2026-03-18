name = input("What's your name? ")

# Append the name to the file
with open("names.txt","a") as file:
    file.write(name+ "\n")

# Read and print all names from the file
with open("names.txt","r") as file:
    for line in file:
        print("Hello,", line.rstrip())