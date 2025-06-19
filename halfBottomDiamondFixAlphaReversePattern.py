'''
E               E 
  D           D
    C       C
      B   B
        A

This program prints an inverted hollow alphabet pyramid:
- Starts from 'E' and decrements to 'A'
- Each row prints the same alphabet at both ends, spaced accordingly
- The last row contains only a single character centered

Author : Sachin Kumar
GitHub : https://github.com/sachin-py/pattern_programs/
'''

n = 5

for i in range(n):
    # Print leading spaces and left character
    print('  ' * i + chr(64 + n - i) + ' ', end='')

    # For rows except the last, print inner spaces and right character
    if i != n - 1:
        print('  ' * (2 * n - 2 * i - 3) + chr(64 + n - i) + ' ', end='')

    print()
