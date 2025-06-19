'''
        E
      D   D
    C       C
  B           B
A               A

This program prints a hollow inverted alphabet pyramid:
- Characters start from 'E' and decrement to 'A'.
- Each row has mirrored characters at both ends.
- Spaces are adjusted to keep the pattern center-aligned.

Author : Sachin Kumar
GitHub : https://github.com/sachin-py/pattern_programs/
'''

n = 5

for i in range(n):
    # Leading spaces + left character
    print('  ' * (n - i - 1) + chr(64 + n - i), end='')
    if i >= 1:
        # Inner spaces + right character (from row 2)
        print('  ' * (2 * i - 1), chr(64 + n - i), end='')
    print()
