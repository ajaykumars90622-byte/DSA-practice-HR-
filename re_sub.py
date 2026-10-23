### Problem: Re.sub() - Regex Substitution

**Problem Statement:**
You are given a text of $n$ lines. The text contains `&&` and `||` symbols. Your task is to modify those symbols to `and` and `or` respectively, ensuring both have a space on both sides, without modifying single `&`/`|` or `&&&`/`|||`.

**Code:**
```python
import re

n = int(input())

for _ in range(n):
    line = input()
    line = re.sub(r'(?<= )&&(?= )', 'and', line)
    line = re.sub(r'(?<= )\|\|(?= )', 'or', line)
    print(line)
