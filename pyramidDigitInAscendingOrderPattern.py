'''
Right-Aligned Increasing Number Triangle Pattern

Pattern for n = 5:

     1 
    1 2
   1 2 3
  1 2 3 4
 1 2 3 4 5

Author : Sachin Kumar
GitHub : https://github.com/sachin-py/pattern_programs/
'''

n = 5

# -----------------------------
# Outer loop controls the number of rows
# Each row begins with (n - i - 1) spaces for right alignment
# Inner loop prints numbers from 1 to (i + 1)
# -----------------------------
for i in range(n):
    print(' ' * (n - i - 1), end=' ')
    for j in range(i + 1):
        print(j + 1, end=' ')
    print()

# -----------------------------
# End of Right-Aligned Number Triangle Pattern
# -----------------------------
