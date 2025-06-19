'''
5 
5 4
5 4 3
5 4 3 2
5 4 3 2 1
5 4 3 2
5 4 3
5 4
5

This program prints a descending number pyramid:
- The first half prints numbers starting from 5 down to (5 - i) on each line.
- The second half mirrors the top half in reverse, decreasing in length.

Author : Sachin Kumar
GitHub : https://github.com/sachin-py/pattern_programs/
'''

n = 5

# Upper half: from 5 down to (5 - i) in each row
for i in range(n):
    for j in range(i + 1):
        print(n - j, end=' ')
    print()

# Lower half: decreasing the range after the middle row
for i in range(n - 1):
    for j in range(n - i - 1):
        print(n - j, end=' ')
    print()
