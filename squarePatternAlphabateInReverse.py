'''
Reverse Column-wise Alphabet Square Pattern Generator

Pattern for n = 5:

E D C B A 
E D C B A
E D C B A
E D C B A
E D C B A

Author : Sachin Kumar
GitHub : https://github.com/sachin-py/pattern_programs/
'''

# -----------------------------
# Reverse Column-wise Alphabet Square
# -----------------------------

n = 5

for i in range(n):
    for j in range(n):
        print(chr(64 + n - j), end=' ')
    print()

# -----------------------------
# End of Reverse Column-wise Alphabet Square Pattern
# -----------------------------
