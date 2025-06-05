'''
Inverted Descending Number Triangle Pattern

Pattern for n = 5:

5 4 3 2 1 
5 4 3 2
5 4 3
5 4
5

Author : Sachin Kumar
GitHub : https://github.com/sachin-py/pattern_programs/
'''

n = 5

# -----------------------------
# Loop to print decreasing length rows of descending numbers starting from n
# -----------------------------
for i in range(n):
    for j in range(n - i):
        print(n - j, end=' ')
    print()

# -----------------------------
# End of Inverted Descending Number Triangle Pattern
# -----------------------------
