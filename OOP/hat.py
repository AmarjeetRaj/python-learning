import random

class Hat:
    # def __init__(self):
    #     self.houses = ["Gryffindor","Slytherin","Hufflepuff","Ravenclaw"]
    houses = ["Gryffindor","Slytherin","Hufflepuff","Ravenclaw"]

    #refers to static class
    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))

if __name__=="__main__":
    # hat = Hat()
    Hat.sort("Harry")