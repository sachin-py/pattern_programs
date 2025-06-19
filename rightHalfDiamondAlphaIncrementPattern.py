'''
A  
A  B
A  B  C
A  B  C  D
A  B  C  D  E
A  B  C  D
A  B  C
A  B
A

This program prints an alphabetical pyramid pattern:
- The first half prints increasing letters from A to the row's length.
- The second half mirrors the top, decreasing back to A.
- Note: There’s an extra line in the middle with E letters, which makes the total lines = 9.

Author : Sachin Kumar
GitHub : https://github.com/sachin-py/pattern_programs/
'''

n = 5

# Upper half: print A to A+row_index
for i in range(n):
    for j in range(i + 1):
        print((chr(65 + j) + ' '), end=' ')
    print()

# Lower half: reverse pattern from (n-1) rows down to 1
for i in range(n - 1):
    for j in range(n - i - 1):
        print((chr(65 + j) + ' '), end=' ')
    print()
