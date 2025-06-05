'''
Inverted Alphabet Repetition Pattern (Descending Letters)

Pattern for n = 5:

E E E E E 
D D D D
C C C
B B
A

Author : Sachin Kumar
GitHub : https://github.com/sachin-py/pattern_programs/
'''

n = 5

# -----------------------------
# Loop to print decreasing repetitions of alphabets starting from 'E' down to 'A'
# -----------------------------
for i in range(n):
    print((chr(64 + n - i) + ' ') * (n - i))

# -----------------------------
# End of Inverted Alphabet Repetition Pattern
# -----------------------------
