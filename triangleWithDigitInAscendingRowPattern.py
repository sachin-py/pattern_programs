'''
Incremental Number Sequence Triangle Pattern

Pattern for n = 5:

1 
1 2
1 2 3
1 2 3 4
1 2 3 4 5

Author : Sachin Kumar
GitHub : https://github.com/sachin-py/pattern_programs/
'''

n = 5

# -----------------------------
# Printing incremental number sequences line by line
# -----------------------------
for i in range(n):
    for j in range(i + 1):
        print(j + 1, end=' ')
    print()

# -----------------------------
# End of Incremental Number Sequence Triangle Pattern
# -----------------------------
