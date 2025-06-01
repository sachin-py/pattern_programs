'''
Alphabet Square Pattern Generator

Pattern for n = 5:

A A A A A
A A A A A
A A A A A
A A A A A
A A A A A

Author : Sachin Kumar
GitHub : https://github.com/sachin-py/pattern_programs/
'''

# -----------------------------
# Method 1: Using string repetition
# -----------------------------

n = 5

for i in range(n):
    print((chr(65) + ' ') * n)


# -----------------------------
# Method 2: Using nested loops
# -----------------------------

print('\nAlternate\n')

for i in range(n):
    for j in range(n):
        print(chr(65) + ' ', end='')
    print()

# -----------------------------
# End of Alphabet Square Pattern
# -----------------------------
