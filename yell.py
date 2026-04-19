def main():
    yell("This", "is", "CS50")

def yell(*words):
    # uppercase = map(str.upper, words)
    # for word in words:
    #     uppercase.append(word.upper())
    uppercase = [word.upper() for word in words]
    print(*uppercase)

if __name__=="__main__":
    main() 