'''
Incremental Alphabet Triangle Pattern

Pattern for n = 5:

A 
B B 
C C C 
D D D D 
E E E E E 

Author : Sachin Kumar
GitHub : https://github.com/sachin-py/pattern_programs/
'''

n = 5

# -----------------------------
# Method 1: Using nested loops
# -----------------------------
for i in range(n):
    for j in range(i + 1):
        print(chr(65 + i), end=' ')
    print()

# -----------------------------
# Method 2: Using string multiplication
# -----------------------------
print('Alternate\n')
for i in range(n):
    print((chr(65 + i) + ' ') * (i + 1))

# -----------------------------
# End of Incremental Alphabet Triangle Pattern
# -----------------------------
