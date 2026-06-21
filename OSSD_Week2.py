# ==========================================
# OSSD WEEK 2 - COMPLETE PROGRAMS FILE
# ==========================================

# 1. Python Variables and Data Types
x = 10
print("Value of x:", x)
print("Type of x:", type(x))

y = 5.75
print("Value of y:", y)
print("Type of y:", type(y))

message = "Hello"
new_message = message + " World"
print("Original message:", message)
print("Concatenated message:", new_message)

# 2. Rectangle Area and Even/Odd Check
length = float(input("\nEnter rectangle length: "))
width = float(input("Enter rectangle width: "))
print("Area:", length * width)

number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# 3. Sum of Two Numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("Sum =", num1 + num2)

# 4. Greeting Message
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Hello {name}! You are {age} years old.")

# 5. Square of a Number
number = float(input("Enter a number: "))
print("Square =", number * number)

# 6. Positive, Negative or Zero
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# 7. Divisible by 5
number = int(input("Enter an integer: "))
if number % 5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible by 5")

# 8. Largest of Three Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest =", a)
elif b >= a and b >= c:
    print("Largest =", b)
else:
    print("Largest =", c)

# 9. Print 1 to 10 using for loop
print("\nNumbers 1 to 10:")
for i in range(1, 11):
    print(i, end=" ")
print()

# 10. First 10 Even Numbers
print("\nFirst 10 Even Numbers:")
count = 1
num = 2
while count <= 10:
    print(num, end=" ")
    num += 2
    count += 1
print()

# 11. Sum from 1 to n
n = int(input("\nEnter n: "))
print("Sum =", sum(range(1, n + 1)))

# 12. Skip 5 using continue
print("\nNumbers 1-10 skipping 5:")
for i in range(1, 11):
    if i == 5:
        continue
    print(i, end=" ")
print()

# 13. Break Example
print("\nEnter numbers (0 to stop):")
while True:
    num = int(input("Enter number: "))
    if num == 0:
        print("Loop Stopped")
        break
    print("You entered:", num)

# 14. Pass Example
print("\nPass Example:")
for i in range(1, 6):
    if i == 3:
        pass
    print(i, end=" ")
print()

# 15. Swap, Concatenate and Sum
a = int(input("\nEnter an integer: "))
b = float(input("Enter a float: "))

original_a = a
original_b = b

a, b = b, a

print("Concatenated:", str(a) + str(b))
print("Sum:", int(original_a + original_b))

# 16. Word Count and Reverse Sentence
sentence = input("\nEnter a sentence: ")
words = sentence.split()

print("Number of words:", len(words))
print("Reversed sentence:", " ".join(words[::-1]))

# 17. Grade Classification
score = int(input("\nEnter score: "))

if score < 0 or score > 100:
    print("Invalid Score")
elif score >= 90:
    print("A")
elif score >= 75:
    print("B")
elif score >= 50:
    print("C")
elif score >= 35:
    print("D")
else:
    print("Fail")

# 18. Prime Numbers from 2 to n
n = int(input("\nEnter a number: "))

print("Prime Numbers:")
for num in range(2, n + 1):
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, end=" ")
print()

# 19. Prime Numbers and Sum using While Loop
n = int(input("\nEnter a number: "))

num = 2
sum_primes = 0
primes = []

while num <= n:
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        primes.append(num)
        sum_primes += num

    num += 1

print("Prime Numbers:", primes)
print("Sum of Primes:", sum_primes)

# 20. First Number Divisible by Divisor
start = int(input("\nEnter start: "))
end = int(input("Enter end: "))
divisor = int(input("Enter divisor: "))

found = False

for num in range(start, end + 1):
    if num < 0:
        continue

    if num % divisor == 0:
        print("First divisible number:", num)
        found = True
        break

if not found:
    print("No valid number found")
