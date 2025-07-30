n = int(input("Enter a number: "))
if n == 0:
    print("The number is zero.")
else:
    print("The number is non-zero.")





print("Find largest of two numbers")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print(f"{a} is larger.")
elif b > a:
    print(f"{b} is larger.")
else:
    print("Both numbers are equal.")




print("Check if a number is positive, negative, or zero")
n = float(input("Enter a number: "))
if n > 0:
    print("The number is positive.")
elif n < 0:
    print("The number is negative.")
else:
    print("The number is zero.")




print("Check if a character is a vowel or consonant")   
ch = input("Enter a character: ").lower()

if ch in 'aeiou':
    print(f"{ch} is a vowel.")
elif ch.isalpha():
    print(f"{ch} is a consonant.")
else:
    print("Invalid input; not an alphabet.")



print("Check if a number is even or odd")
percentage = float(input("Enter student percentage: "))

if percentage >= 90:
    print("Excellent performance")
elif percentage >= 80:
    print("Very Good performance")
elif percentage >= 70:
    print("Good performance")
elif percentage >= 60:
    print("Average performance")
else:
    print("Poor performance")



print("Find the largest of three numbers")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print(f"{a} is the largest.")
elif b >= a and b >= c:
    print(f"{b} is the largest.")
else:
    print(f"{c} is the largest.")


print("Find the smallest of three numbers")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a <= b and a <= c:
    print(f"{a} is the smallest.")
elif b <= a and b <= c:
    print(f"{b} is the smallest.")
else:
    print(f"{c} is the smallest.")


