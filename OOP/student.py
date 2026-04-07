class Student:
     def __init__(self, name="Harry", house="Gryffindor", patronus="Stag"):
          self.name = name
          self.house = house
          self.patronus = patronus
     
     def __str__(self):
          return f"{self.name} from {self.house}"
     
     def charm(self):
          match self.patronus:
               case "Stag":
                    return "🐴"
               case "Otter":
                    return "🦦"
               case "Jack Russell terrier":
                    return "🐶"
               case _:
                    return "🪄"

     @property
     def name(self):
          return self._name
     
     @name.setter
     def name(self, name):
          if not name:
               raise ValueError("Missing Name")
          self._name = name

     @property
     def house(self):
          return self._house

     @house.setter
     def house(self, house):
          if house not in ["Gryffindor","Hufflepuff","Ravenclaw","Slytherin"]:
               raise ValueError("Invalid house")
          self._house = house     
     
     @classmethod
     def get(cls):
          name = input("Name: ")
          house = input("House: ")
          patronus = input("Patronus: ")
          return cls(name, house, patronus)

def main():
#     student = get_student()
#     student.house = "Number Four, Privet Drive"
    student = Student()
    print(Student.get())
    print("Expecto Patronum!")
    print(student.charm())


if __name__ == "__main__":
     main()