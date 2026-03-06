# x = int(input("Enter the repitions:"))

# for i in range(x):
#     print("Meow")

# print("************for loop is done***********")

# while True:
#     n = int(input("Enter a number: "))
#     if n > 0:
#         break;

# for _ in range(n):
#     print("Meow")

# # while x > 0:
# #     print("Meow")
# #     x -= 1
# # print("************while loop is done***********")

# #another feature in python
# print("Meow\n" * x , end="")      

def main():
    meow()

def meow():
    n = get_number()
    for _ in range(n):
        print("Meow")

def get_number():
    while True:
        n = int(input("Enter a number: "))
        if n > 0:
            return n

main()