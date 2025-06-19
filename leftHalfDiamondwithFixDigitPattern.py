'''
      1 
    2 2
  3 3 3
4 4 4 4
  3 3 3
    2 2
      1

This program prints a centered number diamond:
- The top half prints an increasing pyramid of numbers, each row showing the same digit.
- The bottom half mirrors the top, with decreasing rows and increasing leading spaces.

Author : Sachin Kumar
GitHub : https://github.com/sachin-py/pattern_programs/
'''

n = 4

# Top half: numbers increase, leading spaces decrease
for i in range(n):
    print('  ' * (n - i - 1) + (str(i + 1) + ' ') * (i + 1))

# Bottom half: numbers decrease, leading spaces increase
for i in range(n - 1):
    print('  ' * (i + 1) + (str(n - i - 1) + ' ') * (n - i - 1))
