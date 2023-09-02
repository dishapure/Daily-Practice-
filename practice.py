class Student:
    x = "boy you are happy"
    rollnumber = None

    def __init__(self):
        self.name = "olivia"
        self.rollnumber = 99090090909

    def setrollno(self):
        self.rollnumber = 2080890

gai = Student()
gai.setrollno()
print(gai.rollnumber)
