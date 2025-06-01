'''
Number Square Pattern Generator

Pattern for n = 5:

5 5 5 5 
5 5 5 5
5 5 5 5
5 5 5 5

Author : Sachin Kumar
GitHub : https://github.com/sachin-py/pattern_programs/
'''

# -----------------------------
# Method 1: Using string repetition
# -----------------------------

n = 5

for i in range(n):
    print((str(n) + ' ') * n)


# -----------------------------
# Method 2: Using nested loops
# -----------------------------

print('\nAnother way\n')

for i in range(n):
    for j in range(n):
        print(str(n) + ' ', end='')
    print()

# -----------------------------
# End of Number Square Pattern
# -----------------------------
