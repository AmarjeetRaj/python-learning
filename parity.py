def main():
    number = int(input("Enter a number: "))
    if is_even(number):
        print(number, "is even.")
    else:
        print(number, "is odd.")
    
def is_even(n):
    return n % 2 == 0

main()