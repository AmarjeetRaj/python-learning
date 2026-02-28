def main():
    name = input("What is your name?").strip().title()
    hello(name)


def hello(to="World"):
    print("Hello", to)
#print("Hello,",name, sep= "???")

main()
