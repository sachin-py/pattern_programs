'''
Right-Aligned Reversed Number Triangle Pattern

Pattern for n = 5:

    5 
   5 4
  5 4 3
 5 4 3 2
5 4 3 2 1

Author : Sachin Kumar
GitHub : https://github.com/sachin-py/pattern_programs/
'''

n = 5

# -----------------------------
# Outer loop controls the number of rows
# ' ' * (n - i - 1) adds leading spaces for right alignment
# Inner loop prints numbers from n down to (n - i)
# -----------------------------
for i in range(n):
    print(' ' * (n - i - 1), end='')
    for j in range(i + 1):
        print(str(n - j) + ' ', end='')
    print()

# -----------------------------
# End of Reversed Number Triangle Pattern
# -----------------------------
