### Problem: Finding the Percentage

**Problem Statement:**
The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.

**Code:**
```python
if __name__ == '__main__':
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

#Sample Input 0:
#3
#Krishna 67 68 69
#Arjun 70 98 63
#Malika 52 56 60
#Malika

#Sample Output 0:
#56.00
