'''
        5 
      5 4
    5 4 3
  5 4 3 2
5 4 3 2 1
  5 4 3 2
    5 4 3
      5 4
        5

This program prints a mirrored diamond pattern using decreasing numbers:
- The top half increases the number of values printed per row, starting from 5 downwards.
- The bottom half mirrors the top, reducing numbers per row and increasing leading spaces.

Author : Sachin Kumar
GitHub : https://github.com/sachin-py/pattern_programs/
'''

n = 5

# Top half: print decreasing numbers with decreasing spaces
for i in range(n):
    print('  ' * (n - i - 1), end='')          # Leading spaces
    for j in range(i + 1):
        print(n - j, end=' ')                  # Decreasing numbers from n
    print()

# Bottom half: mirror the top with increasing spaces and fewer numbers
for i in range(n):
    print('  ' * (i + 1), end='')              # Leading spaces
    for j in range(n - i - 1):
        print(n - j, end=' ')                  # Decreasing numbers from n
    print()
