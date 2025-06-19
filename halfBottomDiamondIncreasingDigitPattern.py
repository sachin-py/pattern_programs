'''
1               1 
  2           2
    3       3
      4   4
        5

This program prints a hollow number diamond in inverted form:
- Numbers increment from 1 to 5
- Each row has the same number printed on both ends, except the last which prints once
- Spaces increase to create the hollow effect

Author : Sachin Kumar
GitHub : https://github.com/sachin-py/pattern_programs/
'''

n = 5
for i in range(n):
    # Print leading spaces and left number
    print('  ' * i + str(i + 1) + ' ', end='')

    # Print hollow gap and right number (skip last row)
    if i != n - 1:
        print('  ' * (2 * n - 2 * i - 3) + str(i + 1) + ' ', end='')

    print()
