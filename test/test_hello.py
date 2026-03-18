from hello import hello

def main():
    test_argument()

def test_argument():
    assert hello("Alice") == "Hello, Alice"
    assert hello("Bob") == "Hello, Bob"

def test_default():
    assert hello() == "Hello, World"

if __name__ == "__main__":
    main()