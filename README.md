<div align="center">

<style>
@keyframes popFromLeft {
  0% {
    opacity: 0;
    transform: translateX(-50px);
  }
  100% {
    opacity: 1;
    transform: translateX(0);
  }
}

@keyframes fadeIn {
  0% {
    opacity: 0;
    transform: translateY(15px);
  }
  100% {
    opacity: 1;
    transform: translateY(0);
  }
}

.animated-title {
  animation: popFromLeft 0.8s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}

.animated-content {
  opacity: 0;
  animation: fadeIn 0.8s ease-out 0.5s forwards;
}
</style>

<div class="animated-title">

# 🚀 Python Algorithmic Portfolio

</div>

<div class="animated-content">

[![Python 3](https://img.shields.io/badge/Python-3.x-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![GitHub Repo status](https://img.shields.io/badge/Status-Active-success.svg?style=for-the-badge)]()
[![Platform](https://img.shields.io/badge/Platform-HackerRank-orange.svg?style=for-the-badge)]()

*A structured collection of clean, idiomatic Python solutions built for algorithmic problem-solving and software engineering fundamentals.*

</div>

</div>

---

<div class="animated-content">

## 💻 Tech Stack & Core Competencies

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Data_Structures-Lists%20%7C%20Dicts%20%7C%20Sets-blueviolet?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Regex-Pattern_Matching-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" />
</p>

---

## 📂 Completed Programs Index (All 13 Solutions)

| # | Program / Problem Name | Core Concepts & Techniques | Status |
| :---: | :--- | :--- | :---: |
| **01** | Say "Hello, World!" With Python | Basic I/O, Print syntax | `Completed ✅` |
| **02** | Python If-Else | Conditional branching, Control flow | `Completed ✅` |
| **03** | Arithmetic Operators | Basic math operations, Expression evaluation | `Completed ✅` |
| **04** | Division | Float vs. Integer division | `Completed ✅` |
| **05** | Loops | Iteration mechanics, Range loops | `Completed ✅` |
| **06** | Write a Function | Modular code, Leap year logic | `Completed ✅` |
| **07** | Print Function | String concatenation, `end=""`, `sep=""` | `Completed ✅` |
| **08** | Find the Runner-Up Score! | Sets, Sorting, List indexing | `Completed ✅` |
| **09** | List Comprehensions | 3D Grid filtering, Compact syntax | `Completed ✅` |
| **10** | Nested Lists | Multi-dimensional data structures, Custom sorting | `Completed ✅` |
| **11** | Finding the Percentage | Dictionaries, Iteration, Float formatting (`:.2f`) | `Completed ✅` |
| **12** | Re.sub() - Regex Substitution | Regular expressions, Lookarounds (`(?<=)`, `(?=)`), Pattern matching | `Completed ✅` |
| **13** | Lists | Dynamic command parsing, Method routing, State management | `Completed ✅` |

---

## 📜 Master Consolidated Script (`solutions.py`)

<details>
<summary><b>Click to view the complete merged Python source code</b></summary>

```python
# ==========================================
# 01. Say "Hello, World!" With Python
# ==========================================
print("Hello, World!")


# ==========================================
# 02. Python If-Else
# ==========================================
n = int(input().strip())
if n % 2 != 0:
    print("Weird")
elif 2 <= n <= 5:
    print("Not Weird")
elif 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")


# ==========================================
# 03. Arithmetic Operators
# ==========================================
a = int(input())
b = int(input())
print(a + b)
print(a - b)
print(a * b)


# ==========================================
# 04. Division
# ==========================================
a = int(input())
b = int(input())
print(a // b)
print(a / b)


# ==========================================
# 05. Loops
# ==========================================
n = int(input())
for i in range(n):
    print(i ** 2)


# ==========================================
# 06. Write a Function (Leap Year)
# ==========================================
year = int(input())
leap = False
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            leap = True
    else:
        leap = True
print(leap)


# ==========================================
# 07. Print Function
# ==========================================
n = int(input())
for i in range(1, n + 1):
    print(i, end="")
print()


# ==========================================
# 08. Find the Runner-Up Score!
# ==========================================
n = int(input())
arr = map(int, input().split())
unique_scores = sorted(set(arr))
print(unique_scores[-2])


# ==========================================
# 09. List Comprehensions
# ==========================================
x = int(input())
y = int(input())
z = int(input())
n = int(input())

result = [
    [i, j, k]
    for i in range(x + 1)
    for j in range(y + 1)
    for k in range(z + 1)
    if i + j + k != n
]
print(result)


# ==========================================
# 10. Nested Lists
# ==========================================
students = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append([name, score])

grades = sorted(set(student[1] for student in students))
second_lowest = grades[1]

names = sorted(
    student[0] for student in students if student[1] == second_lowest
)
for name in names:
    print(name)


# ==========================================
# 11. Finding the Percentage
# ==========================================
n = int(input())
student_marks = {}
for _ in range(n):
    data = input().split()
    name = data[0]
    marks = list(map(float, data[1:]))
    student_marks[name] = marks

query_name = input()
average = sum(student_marks[query_name]) / len(student_marks[query_name])
print(f"{average:.2f}")


# ==========================================
# 12. Re.sub() - Regex Substitution
# ==========================================
import re

n = int(input())
for _ in range(n):
    line = input()
    line = re.sub(r'(?<= )&&(?= )', 'and', line)
    line = re.sub(r'(?<= )\|\|(?= )', 'or', line)
    print(line)


# ==========================================
# 13. Lists (Dynamic Command Parser)
# ==========================================
N = int(input())
lst = []
for _ in range(N):
    cmd = input().split()
    operation = cmd[0]
    
    if operation == 'insert':
        lst.insert(int(cmd[1]), int(cmd[2]))
    elif operation == 'print':
        print(lst)
    elif operation == 'remove':
        lst.remove(int(cmd[1]))
    elif operation == 'append':
        lst.append(int(cmd[1]))
    elif operation == 'sort':
        lst.sort()
    elif operation == 'pop':
        lst.pop()
    elif operation == 'reverse':
        lst.reverse()
