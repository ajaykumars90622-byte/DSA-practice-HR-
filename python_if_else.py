### Problem: Python If-Else

##**Problem Statement:**
##Given an integer $n$, print `Weird` if it's odd. If it's even, print `Not Weird` for ranges 2 to 5 and greater than 20, and `Weird` for the range 6 to 20.

##**Code:**
n = int(input())
if n % 2 != 0:
    print("Weird")
elif 2 <= n <= 5:
    print("Not Weird")
elif 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")
##Sample Input 0: 3
##Sample Output 0: Weird

##Sample Input 1: 24
##Sample Output 1: Not Weird

##Status: All test cases passed successfully! ✅
