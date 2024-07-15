class Student:
    school = "freeCodeCamp.org"
    
    def __init__(self, name, course):
        self.name = name
        self.course = course
    
Student1 = Student("Jane", "JavaScript")
Student2 = Student("John", "Python")

print(Student1.name) # Jane
print(Student2.name) # John

print(Student1.course)


print(Student1.school) # freeCodeCamp.org
print(Student2.school) # freeCodeCamp.org