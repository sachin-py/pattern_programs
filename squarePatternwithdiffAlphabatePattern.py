'''
Row-wise Alphabet Square Pattern Generator

Pattern for n = 5:

A A A A A
B B B B B
C C C C C
D D D D D
E E E E E

Author : Sachin Kumar
GitHub : https://github.com/sachin-py/pattern_programs/
'''

# -----------------------------
# Method 1: Using string repetition
# -----------------------------

n = 5

for i in range(n):
    print((chr(65 + i) + ' ') * n)


# -----------------------------
# Method 2: Using nested loops
# -----------------------------

print('\nAlternate\n')

for i in range(n):
    for j in range(n):
        print(chr(65 + i) + ' ', end='')
    print()

# -----------------------------
# End of Row-wise Alphabet Square Pattern
# -----------------------------
