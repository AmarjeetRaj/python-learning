#type hints, docstring

import sys
import argparse

if len(sys.argv) == 1:
    print("meow")
else:
    print("usage: meows.py")


def meow(n: int) -> str:
    """
    Meow n times

    :param n: No of times to meow
    :type n: int
    :raise TypeError: If n is not int
    :return: A string of n meows, one per line
    :rtype: str
    """
    return "meow\n" * n

def main():
    number: int = int(input("Number: "))
    meows: str = meow(number)
    print(meows, end="")

def arg_parse():
    parser = argparse.ArgumentParser(description="Meow like a cat")
    parser.add_argument("-n",default=1, help="number of times to meow")
    args = parser.parse_args()

    for _ in range(int(args.n )): print("meow")

if __name__=="__main__":
    arg_parse()