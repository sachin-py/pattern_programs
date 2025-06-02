'''
Reverse Row-wise Alphabet Square Pattern Generator

Pattern for n = 4:

D D D D 
C C C C
B B B B
A A A A

Author : Sachin Kumar
GitHub : https://github.com/sachin-py/pattern_programs/
'''

# -----------------------------
# Method 1: Using string repetition
# -----------------------------

n = 4

for i in range(n):
    print((chr(64 + n - i) + ' ') * n)


# -----------------------------
# Method 2: Using nested loops
# -----------------------------

print('Another Way\n')

for i in range(n):
    for j in range(n):
        print(chr(64 + n - i) + ' ', end='')
    print()

# -----------------------------
# End of Reverse Row-wise Alphabet Square Pattern
# -----------------------------
