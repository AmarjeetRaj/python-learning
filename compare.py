x = int(input("Enter x: "))
y = int(input("Enter y: "))

if x < y :
    print(f"x is less than y")
elif x > y :
    print(f"x is greater than y")
else:
    print(f"x is equal to y")

#refined version
if x < y or x > y :
    print(f"x is not equal to y")
else:
    print(f"x is equal to y")

#more refined version
if x != y :
    print(f"x is not equal to y")
else:
    print(f"x is equal to y")