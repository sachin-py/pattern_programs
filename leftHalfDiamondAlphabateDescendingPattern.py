'''
      D 
    D C
  D C B
D C B A
  D C B
    D C
      D

This program prints a mirrored diamond using reverse alphabets:
- The top half builds from D down to A with decreasing spaces.
- The bottom half mirrors the top with increasing spaces and decreasing letters.

Author : Sachin Kumar
GitHub : https://github.com/sachin-py/pattern_programs/
'''

n = 4

# Top half: reverse letters with decreasing spaces
for i in range(n):
    print('  ' * (n - i - 1), end='')                # Leading spaces
    for j in range(i + 1):
        # Reverse characters from D
        print(chr(64 + n - j), end=' ')
    print()

# Bottom half: mirror the top with increasing spaces
for i in range(n):
    print('  ' * (i + 1), end='')                    # Leading spaces
    for j in range(n - i - 1):
        # Reverse characters from D
        print(chr(64 + n - j), end=' ')
    print()
