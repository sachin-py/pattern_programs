'''
        A 
      A B
    A B C
  A B C D
A B C D E
  A B C D
    A B C
      A B
        A

This program prints a centered diamond using increasing alphabets:
- The top half prints lines with ascending characters from A.
- The bottom half mirrors the top in reverse order, reducing character count per row.

Author : Sachin Kumar
GitHub : https://github.com/sachin-py/pattern_programs/
'''

n = 5

# Top half: increasing letters with decreasing spaces
for i in range(n):
    print('  ' * (n - i - 1), end='')              # Leading spaces
    for j in range(i + 1):
        print(chr(64 + j + 1), end=' ')            # Characters from A upwards
    print()

# Bottom half: decreasing letters with increasing spaces
for i in range(n):
    print('  ' * (i + 1), end='')                  # Leading spaces
    for j in range(n - i - 1):
        print(chr(64 + j + 1), end=' ')            # Characters from A upwards
    print()
