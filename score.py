### Problem: Find the Runner-Up Score!

**Problem Statement:**
Given the participants' score sheet for a University Sports Day, store the scores in a list and find the score of the runner-up without using string methods.

**Code:**
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    unique_scores = sorted(set(arr))
    print(unique_scores[-2])

#Sample Input 0:
#5
#2 3 6 6 5

#Sample Output 0:
#5
