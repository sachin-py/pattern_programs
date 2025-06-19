'''
1 
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1

This program prints a number pyramid:
- The first half prints increasing sequences starting from 1 up to the row number.
- The second half mirrors the top, reducing the length of the sequence by one each row.

Author : Sachin Kumar
GitHub : https://github.com/sachin-py/pattern_programs/
'''

n = 5

# Upper half: increasing number sequence
for i in range(n):
    for j in range(i + 1):
        print(j + 1, end=' ')
    print()

# Lower half: decreasing number sequence
for i in range(n - 1):
    for j in range(n - i - 1):
        print(j + 1, end=' ')
    print()
