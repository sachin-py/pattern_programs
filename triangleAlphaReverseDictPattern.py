'''
Reverse Alphabet Triangle Pattern

Pattern for n = 5:

E 
E D
E D C
E D C B
E D C B A

Author : Sachin Kumar
GitHub : https://github.com/sachin-py/pattern_programs/
'''

n = 5

# -----------------------------
# Loop to print alphabets in reverse starting from 'E' in each row
# -----------------------------
for i in range(n):
    for j in range(i + 1):
        print(chr(64 + n - j), end=' ')
    print()

# -----------------------------
# End of Reverse Alphabet Triangle Pattern
# -----------------------------
