'''
Reverse Column-wise Number Square Pattern Generator

Pattern for n = 5:

5 4 3 2 1 
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1

Author : Sachin Kumar
GitHub : https://github.com/sachin-py/pattern_programs/
'''

# -----------------------------
# Reverse Column-wise Number Square
# -----------------------------

n = 5

for i in range(n):
    for j in range(n):
        print(n - j, end=' ')
    print()

# -----------------------------
# End of Reverse Column-wise Number Square Pattern
# -----------------------------
