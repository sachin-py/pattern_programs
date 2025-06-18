'''
Right-Aligned Alphabet Triangle Pattern

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
# Loop to print a right-aligned triangle of increasing alphabets
# Each row has leading spaces and then repeats the corresponding alphabet
# chr(65) gives 'A', 66 -> 'B', etc.
# -----------------------------
for i in range(n):
    print(' ' * (n - i - 1) + (chr(65 + i) + ' ') * (i + 1))

# -----------------------------
# End of Right-Aligned Alphabet Triangle Pattern
# -----------------------------
