'''
        1 
      2   2
    3       3
  4           4
5               5

This program prints a hollow number pyramid:
- Numbers increase from 1 to n and are printed at both ends of each row.
- Middle space grows with each level, starting from row 2.
- The triangle is center-aligned with appropriate leading spaces.

Author : Sachin Kumar
GitHub : https://github.com/sachin-py/pattern_programs/
'''

n = 5

for i in range(n):
    # Leading spaces + left number
    print('  ' * (n - i - 1) + str(i + 1) + ' ', end='')
    if i >= 1:
        # Inner spaces + right number (from row 2)
        print('  ' * (2 * i - 1) + str(i + 1), end='')
    print()
