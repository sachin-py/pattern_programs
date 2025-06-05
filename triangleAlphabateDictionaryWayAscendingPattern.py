'''
Alphabet Incremental Triangle Pattern

Pattern for n = 5:

A 
A B
A B C
A B C D
A B C D E

Author : Sachin Kumar
GitHub : https://github.com/sachin-py/pattern_programs/
'''

n = 5

# -----------------------------
# Loop to print increasing alphabet sequence row by row
# -----------------------------
for i in range(n):
    for j in range(i + 1):
        print(chr(65 + j), end=' ')
    print()

# -----------------------------
# End of Alphabet Incremental Triangle Pattern
# -----------------------------
