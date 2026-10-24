class Student:
    def __init__(self,name,major,gender,math,physics,chemistry):
        self.name = name
        self.major = major
        self.gender = gender
        self.math = math
        self.physics = physics
        self.chemistry = chemistry

    def greet(self):
            print(f"Students name is {self.name}, he/she studies {self.major} and his/her gender is {self.gender}")

    def mesatarja(self):
            print (f"{self.name}'s avarage is {(self.math + self.physics + self.chemistry)/3}")

student1 = Student("Enes","Programming","M",10,9,8)
student2 = Student("Elvis","Physics","M",8,10,7)

student1.greet()
student2.greet()

student1.mesatarja()
student2.mesatarja()