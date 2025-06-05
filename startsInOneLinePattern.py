'''
Simple Horizontal Star Line Pattern

Pattern for n = 3:

* * * 
Another way
* * *

Author : Sachin Kumar
GitHub : https://github.com/sachin-py/pattern_programs/
'''

n = 3

# -----------------------------
# Method 1: Using loop and print with end=' '
# -----------------------------
for i in range(n):
    print('*', end=' ')
print()

# -----------------------------
# Method 2: Using string multiplication
# -----------------------------
print('Another way')
print('* ' * n)

# -----------------------------
# End of Simple Horizontal Star Line Pattern
# -----------------------------
