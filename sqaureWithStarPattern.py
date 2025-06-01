'''
Solid Square Pattern Generator

Pattern for n = 4:

* * * * 
* * * *
* * * *
* * * *

Author : Sachin Kumar
GitHub : https://github.com/sachin-py/pattern_programs/
'''

# -----------------------------
# Method 1: Using string repetition
# -----------------------------

n = 4

for i in range(n):
    print('* ' * n)


# -----------------------------
# Method 2: Using nested loops
# -----------------------------

print('\nAnother way\n')

for i in range(n):
    for j in range(n):
        print('* ', end='')
    print()

# -----------------------------
# End of Solid Square Pattern
# -----------------------------
