class Student():
    name = ""
    dept = ""
    uid = ""

    def __init__(self, name,dept, uid):
        self.name = name
        self.dept = dept
        self.uid  = uid

    def __str__(self):
        return self.name+" "+self.dept+" "+self.uid

#create an obejct
student = Student("shukumar", "cse", "10542")
#print(student.name , student.dept,student.uid)
print(student)