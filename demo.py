a=3
b=5
print(a+b)

name = "Tejal"
age = 19
height = 5.4
is_student = True
fav_subjects = ["Python", "Math", "ML"]
dob = (23, "October", 2005)
profile = {
    "Name": name,
    "Age": age,
    "Height": height,
    "Student": is_student,
    "Subjects": fav_subjects,
    "DOB": dob
}

print("Profile Summary:")
print(f"Name: {profile['Name']}")
print(f"Age: {profile['Age']}")
print(f"Height: {profile['Height']} ft")
print(f"Is Student? {profile['Student']}")
print(f"Favorite Subjects: {', '.join(profile['Subjects'])}")
print(f"Date of Birth: {profile['DOB'][0]} {profile['DOB'][1]} {profile['DOB'][2]}")



