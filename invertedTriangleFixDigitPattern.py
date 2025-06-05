'''
Inverted Number Triangle Pattern

Pattern for n = 5:

1 1 1 1 1 
2 2 2 2
3 3 3
4 4
5

Author : Sachin Kumar
GitHub : https://github.com/sachin-py/pattern_programs/
'''

n = 5

# -----------------------------
# Loop to print decreasing repetition of numbers from 1 to n
# -----------------------------
for i in range(n):
    print((str(i + 1) + ' ') * (n - i))

# -----------------------------
# End of Inverted Number Triangle Pattern
# -----------------------------
