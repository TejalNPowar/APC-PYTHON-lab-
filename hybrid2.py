# Parent class
class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def display_student(self):
        print(f"Student Name: {self.name}, Roll No: {self.roll}")


# Inherited by Exam (Single → Multilevel)
class Exam(Student):
    def __init__(self, name, roll, marks):
        super().__init__(name, roll)
        self.marks = marks

    def display_exam(self):
        print(f"Exam Marks: {self.marks}")


# Another parent class (for multiple inheritance)
class Project:
    def __init__(self, project_title):
        self.project_title = project_title

    def display_project(self):
        print(f"Project Title: {self.project_title}")


# Result inherits from both Exam and Project → Hybrid
class Result(Exam, Project):
    def __init__(self, name, roll, marks, project_title):
        Exam.__init__(self, name, roll, marks)
        Project.__init__(self, project_title)

    def display_result(self):
        self.display_student()
        self.display_exam()
        self.display_project()


# Example usage
r = Result("Tejal", 101, 89, "Smart Canteen System")
r.display_result()
