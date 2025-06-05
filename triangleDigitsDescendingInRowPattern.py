'''
Reverse Number Triangle Pattern

Pattern for n = 5:

5 
5 4
5 4 3
5 4 3 2
5 4 3 2 1

Author : Sachin Kumar
GitHub : https://github.com/sachin-py/pattern_programs/
'''

n = 5

# -----------------------------
# Loop to print decreasing sequences from 'n' down to (n - i)
# -----------------------------
for i in range(n):
    for j in range(i + 1):
        print(n - j, end=' ')
    print()

# -----------------------------
# End of Reverse Number Triangle Pattern
# -----------------------------
