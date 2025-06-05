'''
Incremental Number Triangle Pattern

Pattern for n = 4:

1 
2 2
3 3 3
4 4 4 4

Author : Sachin Kumar
GitHub : https://github.com/sachin-py/pattern_programs/
'''

n = 4

# -----------------------------
# Method 1: Using nested loops
# -----------------------------
for i in range(n):
    for j in range(i + 1):
        print(str(i + 1), end=' ')
    print()

# -----------------------------
# Method 2: Using string multiplication
# -----------------------------
print('Alternate\n')
for i in range(n):
    print((str(i + 1) + ' ') * (i + 1))

# -----------------------------
# End of Incremental Number Triangle Pattern
# -----------------------------
