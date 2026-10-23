### Problem: Nested Lists

**Problem Statement:**
Given the names and grades for each student in a class of $N$ students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade. If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

**Code:**
```python
if __name__ == '__main__':
    students = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    grades = sorted(set(student[1] for student in students))
    second_lowest = grades[1]

    names = sorted(
        student[0]
        for student in students
        if student[1] == second_lowest
    )

    for name in names:
        print(name)

#Sample Input 0:
#5
#Harry
#37.21
#Berry
#37.21
#Tina
#37.2
#Akriti
#41
#Harsh
#39

#Sample Output 0:
#Berry
#Harry
