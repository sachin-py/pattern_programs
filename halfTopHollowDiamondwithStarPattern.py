'''
        * 
      *   *
    *       *
  *           *
*               *

This program prints a hollow pyramid or triangle with a space between the two stars on each row,
starting with one star and widening the gap with each subsequent row.

Author : Sachin Kumar
GitHub : https://github.com/sachin-py/pattern_programs/
'''

n = 5

for i in range(n):
    print('  ' * (n - i - 1) + '* ', end='')      # Leading spaces + left star
    if i >= 1:
        # Inner spaces + right star (from row 2 onward)
        print('  ' * (2 * i - 1) + '*', end='')
    print()
