### Problem: Lists

**Problem Statement:**
Consider a list (`lst = []`). You can perform various commands such as `insert`, `print`, `remove`, `append`, `sort`, `pop`, and `reverse`. Initialize your list and read in the value of $N$ followed by $N$ lines of commands. Iterate through each command in order and perform the corresponding operation on your list.

**Code:**
if __name__ == '__main__':
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

#Sample Input 0:
#12
#insert 0 5
#insert 1 10
#insert 0 6
#print
#remove 6
#append 9
#append 1
#sort
#print
#pop
#reverse
#print

#Sample Output 0:
#[6, 5, 10]
#[1, 5, 9, 10]
#[9, 5, 1]
