'''
5               5
  4           4
    3       3
      2   2
        1

This program prints an inverted hollow number pyramid:
- Numbers descend from 5 to 1.
- Each row has numbers at both ends with increasing leading and inner spaces.
- The last row has only a single number centered.

Author : Sachin Kumar
GitHub : https://github.com/sachin-py/pattern_programs/
'''

n = 5

# Main logic using if-else for last row
for i in range(n):
    if i != n - 1:
        print('  ' * i + str(n - i) + ' ' + '  ' *
              (2 * n - 2 * i - 3) + str(n - i))
    else:
        print('  ' * (n - 1) + str(n - i))

print("\n Alternate \n")

# Alternate way using consistent structure
for i in range(n):
    print('  ' * i + str(n - i) + ' ', end='')
    if i != n - 1:
        print('  ' * (2 * n - 2 * i - 3) + str(n - i) + ' ', end='')
    print()
