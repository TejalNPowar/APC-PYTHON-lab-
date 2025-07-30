print("This program prints numbers from 1 to n using a while loop.")
n = int(input("Enter n: "))
i = 1
while i <= n:
    print(i, end=' ')
    i += 1


print("\nThis program prints numbers from 1 to n using a while loop.")
n = int(input("Enter n: "))
i = 2
while i <= n:
    print(i, end=' ')
    i += 2


print("\nThis program prints odd numbers from 1 to n using a while loop.")
n = int(input("Enter n: "))
i = 1
while i <= n:
    print(i, end=' ')
    i += 2


print("\nSum of first n natural numbers using a while loop")
n = int(input("Enter n: "))
i = 1
sum = 0
while i <= n:
    sum += i
    i += 1
print("Sum:", sum)


print("\nSum of even numbers from 1 to n using a while loop")
n = int(input("Enter n: "))
i = 1
sum = 0
while i <= n:
    sum += i
    i += 2
print("Sum of odd numbers:", sum)



print("\nSum of even numbers from 1 to n using a while loop")
n = int(input("Enter n: "))
i = 2
sum = 0
while i <= n:
    sum += i
    i += 2
print("Sum of even numbers:", sum)



print("\nSum of even numbers from 1 to n using a while loop")
n = int(input("Enter n: "))
i = 2
sum = 0
while i <= n:
    sum += i
    i += 2
print("Sum of even numbers:", sum)


print("\nPrint numbers from n to 1 using a while loop")
n = int(input("Enter n: "))
while n >= 1:
    print(n, end=' ')
    n -= 1




print("\nFibonacci series up to n terms using a while loop")
n = int(input("Enter number of terms: "))
a, b = 0, 1
i = 0
while i < n:
    print(a, end=' ')
    a, b = b, a + b
    i += 1


print("\nFactorial of a number using a while loop")
n = int(input("Enter a number: "))
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
print("Factorial:", fact)



print("\nCheck if a number is prime using a while loop")
num = int(input("Enter a number: "))
if num < 2:
    print("Not a Prime")
else:
    i = 2
    is_prime = True
    while i <= num // 2:
        if num % i == 0:
            is_prime = False
            break
        i += 1
    print("Prime" if is_prime else "Not a Prime")




print("\nSum of digits of a number using a while loop")
num = int(input("Enter a number: "))
sum_digits = 0
while num > 0:
    sum_digits += num % 10
    num //= 10
print("Sum of digits:", sum_digits)



print("\nCheck if a number is a palindrome using a while loop")
num = int(input("Enter a number: "))
original = num
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10
print("Palindrome" if original == reverse else "Not a Palindrome")


print("\nReverse a number using a while loop")
num = int(input("Enter a number: "))
reverse = 0
while num > 0:
    reverse = reverse * 10 + num % 10
    num //= 10
print("Reversed number:", reverse)


print("\nMultiplication table of a number using a while loop")
num = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i += 1


print("\nFind the largest number among n numbers using a while loop")
n = int(input("How many numbers? "))
i = 1
largest = float('-inf')
while i <= n:
    num = int(input(f"Enter number {i}: "))
    if num > largest:
        largest = num
    i += 1
print("Largest number:", largest)


print("\nFind the smallest number among n numbers using a while loop")
n = int(input("How many numbers? "))
i = 1
smallest = float('inf')
while i <= n:
    num = int(input(f"Enter number {i}: "))
    if num < smallest:
        smallest = num
    i += 1
print("Smallest number:", smallest)
