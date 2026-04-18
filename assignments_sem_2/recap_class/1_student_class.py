"""
1. Create a class Student with the following:
• Data members: name, roll_no, marks
• A constructor to initialize the values
• Member functions:
o display_details() → to display student information
o calculate_grade() → to return grade based on marks:
▪ ≥ 90 → A
▪ ≥ 75 → B
▪ ≥ 50 → C
▪ < 50 → Fail

Create at least 3 student objects. Call both functions for each object

"""
class Student:
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks

    def display_details(self):
        print("Name of student: ", self.name)
        print("Roll no: ", self.roll_no)
        print("Marks: ",self.marks)
    
    def calculate_grade(self):
        if self.marks >= 90:
            print("Grade A")
        elif self.marks >= 75:
            print("Grade B")
        elif self.marks >= 50:
            print("Grade C")
        else:
            print("Fail")
        
s1=Student("Alexa",27,98)
s2=Student("Bella",89,78)
s3=Student("Charlie",54,65)

s1.display_details()
s1.calculate_grade()

s2.display_details()
s2.calculate_grade()

s3.display_details()
s3.calculate_grade()