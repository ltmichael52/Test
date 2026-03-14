# class Dog:
#     leg = 4
#     breed = ''

#     def show(doiTuong):
#         print("Số chân của loài chó đó: ",doiTuong.leg)
#         print("Giống chó của đối tượng: ",doiTuong.breed)
    
#     def bark(doiTuong):
#         print("Gâu gâu")


# pitbull = Dog()
# print("Giống chó của đối tượng pitbull: ",pitbull.breed)
# pitbull.breed= 'pitbull'
# print("Giống chó của đối tượng pitbull: ",pitbull.breed)

# pitbull.show()
# pitbull.bark()

#Ctrl + /

class Student:
    name = ''
    math = 0
    literature = 0
    english = 0

    def showInfoStudent(obj1): 
        print("Student name: ",obj1.name)
        print("Math score: ",obj1.math)
        print("Literature score: ",obj1.literature)
        print("English score: ",obj1.english)
        print("Average score: ",obj1.averageScore())
        print("Student rank: ",obj1.showRank())
    
    def averageScore(obj1):
        return (obj1.math+obj1.literature+obj1.english)/3 
    
    def showRank(obj1):
        avg = obj1.averageScore()
        if avg >= 8 :
            print("Excellent")
        elif avg >=6.5:
            print("Good")
        elif avg >=5 :
            print("Average")
        else:
            print("Weak")


std1 = Student()
std1.name = input("Enter student name: ")
std1.math = float(input("Enter student math score: "))
std1.literature = float(input("Enter student literature score: "))
std1.english = float(input("Enter student english score: "))

std1.showInfoStudent()