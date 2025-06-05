'''
Inverted Alphabet Sequence Triangle Pattern

Pattern for n = 5:

A B C D E 
A B C D
A B C
A B
A

Author : Sachin Kumar
GitHub : https://github.com/sachin-py/pattern_programs/
'''

n = 5

# -----------------------------
# Loop to print decreasing length rows of alphabets starting from 'A'
# -----------------------------
for i in range(n):
    for j in range(n - i):
        print(chr(65 + j), end=' ')
    print()

# -----------------------------
# End of Inverted Alphabet Sequence Triangle Pattern
# -----------------------------
