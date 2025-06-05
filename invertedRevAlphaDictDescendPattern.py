'''
Inverted Descending Alphabet Triangle Pattern

Pattern for n = 5:

E D C B A 
E D C B
E D C
E D
E

Author : Sachin Kumar
GitHub : https://github.com/sachin-py/pattern_programs/
'''

n = 5

# -----------------------------
# Loop to print decreasing length rows of alphabets descending from 'E'
# -----------------------------
for i in range(n):
    for j in range(n - i):
        print(chr(64 + n - j), end=' ')
    print()

# -----------------------------
# End of Inverted Descending Alphabet Triangle Pattern
# -----------------------------
