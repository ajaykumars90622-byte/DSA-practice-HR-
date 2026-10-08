### Problem: Print Function

**Problem Statement:**
The included code stub reads an integer, $n$, from STDIN. Without using any string methods, print the list of integers from $1$ through $n$ as a single string without spaces.

**Code:**
n = int(input())

for i in range(1, n + 1):
    print(i, end="")

#Sample Input 0:
#3

#Sample Output 0:
#123
