
print("This program prints numbers from 1 to n using a for loop.")
n = int(input("Enter n: "))
for i in range(1, n+1):
    print(i, end=' ')


print("\nThis program prints even numbers from 1 to n using a for loop.")
n = int(input("Enter n: "))
for i in range(2, n+1, 2):
    print(i, end=' ')


print("\nThis program prints odd numbers from 1 to n using a for loop.")
n = int(input("Enter n: "))
for i in range(1, n+1, 2):
    print(i, end=' ')


print("\nSum of first n natural numbers using a for loop")
n = int(input("Enter n: "))
value = 1
while value <= n**2:
    print(value, end=' ')
    value *= 2


print("\nSum of odd numbers from 1 to n using a for loop")
import math

n = int(input("Enter n: "))
sum_series = 1  # starting with 1
for i in range(1, n+1):
    sum_series += 1 / math.factorial(i)
print("Sum of series:", sum_series)





print("\nSum of even numbers from 1 to n using a for loop")
import math

x = float(input("Enter value of x (in radians): "))
n = int(input("Enter number of terms: "))

cos_x = 0
for i in range(n):
    term = ((-1)**i) * (x**(2*i)) / math.factorial(2*i)
    cos_x += term
print("cos(x) =", cos_x)





print("\nCheck if a number is a perfect square and if its square root is prime")
import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

num = int(input("Enter number: "))
sqrt_num = math.isqrt(num)

if sqrt_num * sqrt_num == num:
    print(f"Square root is {sqrt_num}")
    if is_prime(sqrt_num):
        print("Square root is a prime number.")
    else:
        print("Square root is not a prime number.")
else:
    print("The number is not a perfect square.")





print("\nNested for loop example")
for i in range(3):
    for ch in ['A', 'B', 'C']:
        print(ch, end=' ')
    print()



