'''
      1 
    1 2
  1 2 3
1 2 3 4
  1 2 3
    1 2
      1

This program prints a centered diamond using ascending numbers:
- The top half builds increasing number sequences starting from 1.
- The bottom half mirrors the top in reverse, reducing numbers per row.

Author : Sachin Kumar
GitHub : https://github.com/sachin-py/pattern_programs/
'''

n = 4

# Top half: increasing number sequences, spaces decrease
for i in range(n):
    print('  ' * (n - i - 1), end='')      # Leading spaces
    for j in range(i + 1):
        print(j + 1, end=' ')              # Numbers from 1 to i+1
    print()

# Bottom half: decreasing number sequences, spaces increase
for i in range(n):
    print('  ' * (i + 1), end='')          # Leading spaces
    for j in range(n - i - 1):
        print(j + 1, end=' ')              # Numbers from 1 to (n-i-1)
    print()
