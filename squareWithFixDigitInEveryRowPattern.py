'''
Row-wise Number Square Pattern Generator

Pattern for n = 4:

1 1 1 1 
2 2 2 2
3 3 3 3
4 4 4 4

Author : Sachin Kumar
GitHub : https://github.com/sachin-py/pattern_programs/
'''

# -----------------------------
# Method 1: Using string repetition
# -----------------------------

n = 4

for i in range(n):
    print((str(i + 1) + ' ') * n)


# -----------------------------
# Method 2: Using nested loops
# -----------------------------

print('\nAlternate\n')

for i in range(n):
    for j in range(n):
        print(str(i + 1) + ' ', end='')
    print()

# -----------------------------
# End of Row-wise Number Square Pattern
# -----------------------------
