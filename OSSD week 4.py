# ==========================================
# LISTS PRACTICE TASKS
# ==========================================


movies = ["Inception", "Avatar", "Titanic", "Interstellar", "Joker"]
print(movies[:3])


numbers = [1, 2, 3, 2, 4, 2, 5]
num = 2

while num in numbers:
    numbers.remove(num)

print(numbers)


numbers = [1, 2, 3, 4, 5]
reversed_list = []

for item in numbers:
    reversed_list.insert(0, item)

print(reversed_list)

# ==========================================
# TUPLES PRACTICE TASKS
# ==========================================

numbers = (10, 5, 30, 15, 20)
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))


t = (1, 2, 3, 4)

lst = list(t)
lst[1] = 20

t = tuple(lst)
print(t)


t = (10, 20)

a, b = t
t = (b, a)

print(t)

# ==========================================
# DICTIONARY PRACTICE TASKS
# ==========================================


students = {
    "Ali": 85,
    "Ahmed": 90,
    "Sara": 88
}

print(students)


top_student = max(students, key=students.get)

print("Top Student:", top_student)
print("Marks:", students[top_student])


dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

merged = {**dict1, **dict2}
print(merged)

# ==========================================
# SET PRACTICE TASKS
# ==========================================


numbers = [1, 2, 2, 3, 4, 4, 5]

unique = list(set(numbers))
print(unique)

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A & B)


A = {1, 2}
B = {1, 2, 3, 4}

print(A.issubset(B))

# ==========================================
# WEEKLY CHALLENGES
# ==========================================

numbers = [10, 5, 30, 2, 25]

print("Max:", max(numbers))
print("Min:", min(numbers))


numbers = [1, 2, 2, 3, 2, 4]

print(numbers.count(2))


numbers = [1, 2, 3, 4, 5]

if numbers == sorted(numbers):
    print("Sorted")
else:
    print("Not Sorted")


numbers = [1, 2, 3, 4, 5, 6]

total = 0

for n in numbers:
    if n % 2 == 0:
        total += n

print(total)


def second_largest(lst):
    unique = list(set(lst))
    unique.sort()
    return unique[-2]

print(second_largest([10, 20, 30, 40, 50]))


a = [1, 3, 5]
b = [2, 4, 6]

merged = []
i = j = 0

while i < len(a) and j < len(b):
    if a[i] < b[j]:
        merged.append(a[i])
        i += 1
    else:
        merged.append(b[j])
        j += 1

merged.extend(a[i:])
merged.extend(b[j:])

print(merged)


lst = [1, 2, 3, 4, 5]
n = 2

result = lst[-n:] + lst[:-n]

print(result)


numbers = [1, 2, 2, 3, 4, 4, 5]

unique = []

for n in numbers:
    if n not in unique:
        unique.append(n)

print(unique)


a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

common = []

for item in a:
    if item in b:
        common.append(item)

print(common)


numbers = [1, 2, 3, 4, 5, 6]

mid = len(numbers) // 2

print(numbers[:mid])
print(numbers[mid:])


numbers = [1, 2, 3, 4, 5]
target = 6

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            print(numbers[i], numbers[j])


def left_shift(lst, n):
    return lst[n:] + lst[:n]

def right_shift(lst, n):
    return lst[-n:] + lst[:-n]

numbers = [1, 2, 3, 4, 5]

print(left_shift(numbers, 2))
print(right_shift(numbers, 2))


numbers = [1, 2, 5, 3, 4, 6]

lis = [numbers[0]]

for i in range(1, len(numbers)):
    if numbers[i] > lis[-1]:
        lis.append(numbers[i])

print(lis)

stack = []

stack.append(10)
stack.append(20)
stack.append(30)

print("Peek:", stack[-1])

print("Pop:", stack.pop())

print(stack)


def is_palindrome(lst):
    return lst == lst[::-1]

print(is_palindrome([1, 2, 3, 2, 1]))