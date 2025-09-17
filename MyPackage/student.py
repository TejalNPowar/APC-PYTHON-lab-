class Student:
    # Constructor
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        print(f"Constructor called: Student {self.name} with Roll No {self.roll_no} created")

    # Destructor
    def __del__(self):
        print(f"Destructor called: Student {self.name} with Roll No {self.roll_no} destroyed")
