class Student:
    name = ''
    math = 0


class Student1:
    def __init__(self,name1,math1):
        print("Constructor running")
        self.name = name1
        self.math = math1



std = Student()
std.name = "Phát"
std.math =7

std1 = Student1("Phát",7)

print("Student: ",std.name)
print("Math score student: ",std.math)

print("Student: ",std1.name)
print("Math score student: ",std1.math)
