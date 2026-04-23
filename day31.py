print("---------***********VARUN INSTITUTE Details*************--------")

class Student:
    def __init__(self, Name, Age, EducationalBackground, ID):
        self.Name = Name
        self.Age = Age
        self.EducationalBackground = EducationalBackground
        self.ID = ID

    def display(self):
        print("Name:", self.Name)
        print("Age:", self.Age)
        print("Educational Background:", self.EducationalBackground)
        print("ID:", self.ID)   


class Professor:   
    def __init__(self, Name, Age, Subject, Salary, ID):
        self.Name = Name
        self.Age = Age
        self.Subject = Subject
        self.Salary = Salary
        self.ID = ID

    def display(self):
        print("Name:", self.Name)
        print("Age:", self.Age)
        print("Subject:", self.Subject)
        print("Salary:", self.Salary)
        print("ID:", self.ID)



s1 = Student("Varun", 22, "B.Tech", 23456)
p1 = Professor("Bhanu", 28, "Python", 80000, 101)


s1.display()
p1.display()
