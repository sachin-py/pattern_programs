'''
        5
      4   4
    3       3
  2           2
1               1

This program prints a hollow inverted number pyramid:
- Numbers decrease from 5 to 1 and are printed on both ends of each row.
- Leading spaces align the pyramid centrally.
- Inner space increases with each level (starting from row 2).

Author : Sachin Kumar
GitHub : https://github.com/sachin-py/pattern_programs/
'''

n = 5

for i in range(n):
    # Leading spaces + left number
    print('  ' * (n - i - 1) + str(n - i), end='')
    if i >= 1:
        # Inner spaces + right number (from row 2)
        print('  ' * (2 * i - 1), str(n - i), end='')
    print()
