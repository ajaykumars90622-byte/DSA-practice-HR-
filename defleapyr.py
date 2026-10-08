### Problem: Write a Function (Leap Year)

**Problem Statement:**
Given a year, determine whether it is a leap year according to the Gregorian calendar rules:
- The year can be evenly divided by 4, unless:
  - The year can be evenly divided by 100, then it is NOT a leap year, unless:
    - The year is also evenly divisible by 400. Then it is a leap year.

**code:**
def is_leap(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

year = int(input())
print(is_leap(year))

#Sample Input 0:
#1990

#Sample Output 0:
#False

