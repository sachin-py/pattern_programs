'''
      A
    B   B
  C       C
D           D

This program prints a hollow alphabet pyramid:
- Alphabets increase from A onward and are printed at the edges of the pyramid.
- Leading spaces align the pyramid centrally.
- Inner space increases with each level (starting from row 2).

Author : Sachin Kumar
GitHub : https://github.com/sachin-py/pattern_programs/
'''

n = 4

for i in range(n):
    # Leading spaces + left alphabet
    print('  ' * (n - i - 1) + chr(65 + i), end='')
    if i >= 1:
        # Inner spaces + right alphabet (from row 2)
        print('  ' * (2 * i - 1), chr(65 + i), end='')
    print()
