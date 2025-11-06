class AgeTooSmallError(Exception):
    def __init__(self, message="Age must be at least 18!"):
        self.message = message
        super().__init__(self.message)

try:
    age = int(input("Enter your age: "))
    if age < 18:
        raise AgeTooSmallError
    print("You are eligible!")

except AgeTooSmallError as e:
    print("Error:", e)
