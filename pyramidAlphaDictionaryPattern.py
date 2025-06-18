'''
Right-Aligned Increasing Alphabet Triangle Pattern

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
# Outer loop for number of rows
# Each row starts with (n - i - 1) spaces for alignment
# Inner loop prints characters from 'A' to the corresponding letter
# chr(65 + j) gives 'A', 'B', ..., depending on j
# -----------------------------
for i in range(n):
    print(' ' * (n - i - 1), end=' ')
    for j in range(i + 1):
        print(chr(65 + j), end=' ')
    print()

# -----------------------------
# End of Right-Aligned Alphabet Triangle Pattern
# -----------------------------
