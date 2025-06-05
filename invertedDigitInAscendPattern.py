'''
Inverted Increasing Number Triangle Pattern

Pattern for n = 5:

1 2 3 4 5 
1 2 3 4
1 2 3
1 2
1

Author : Sachin Kumar
GitHub : https://github.com/sachin-py/pattern_programs/
'''

n = 5

# -----------------------------
# Loop to print decreasing length rows of increasing numbers starting from 1
# -----------------------------
for i in range(n):
    for j in range(n - i):
        print(j + 1, end=' ')
    print()

# -----------------------------
# End of Inverted Increasing Number Triangle Pattern
# -----------------------------
