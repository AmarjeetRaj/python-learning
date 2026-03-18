import sys

if len(sys.argv) < 2:
    print("Usage: python cmdline.py [name]")
    sys.exit(1)

for arg in sys.argv[1:]:
    print(arg)

print("Hello, my name is ", sys.argv[1])