'''
Column-wise Alphabet Square Pattern Generator

Pattern for n = 5:

A B C D E 
A B C D E
A B C D E
A B C D E
A B C D E

Author : Sachin Kumar
GitHub : https://github.com/sachin-py/pattern_programs/
'''

# -----------------------------
# Column-wise Alphabet Square
# -----------------------------

n = 5

for i in range(n):
    for j in range(n):
        print(chr(65 + j), end=' ')
    print()

# -----------------------------
# End of Column-wise Alphabet Square Pattern
# -----------------------------
