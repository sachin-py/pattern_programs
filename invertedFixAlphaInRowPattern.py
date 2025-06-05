'''
Inverted Alphabet Repetition Pattern

Pattern for n = 5:

A A A A A 
B B B B
C C C
D D
E

Author : Sachin Kumar
GitHub : https://github.com/sachin-py/pattern_programs/
'''

n = 5

# -----------------------------
# Loop to print decreasing repetitions of each alphabet starting from 'A'
# -----------------------------
for i in range(n):
    print(str(chr(65 + i) + ' ') * (n - i))

# -----------------------------
# End of Inverted Alphabet Repetition Pattern
# -----------------------------
