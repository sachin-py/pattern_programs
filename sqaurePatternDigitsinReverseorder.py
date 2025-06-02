'''
Reverse Row-wise Number Square Pattern Generator

Pattern for n = 5:

5  5  5  5  5  
4  4  4  4  4
3  3  3  3  3
2  2  2  2  2
1  1  1  1  1

Author : Sachin Kumar
GitHub : https://github.com/sachin-py/pattern_programs/
'''

# -----------------------------
# Method 1: Using string repetition
# -----------------------------

n = 5

for i in range(n):
    print((str(n - i) + ' ') * n)


# -----------------------------
# Method 2: Using nested loops
# -----------------------------

print('Another Way\n')

for i in range(n):
    for j in range(n):
        print(str(n - i) + ' ', end='')
    print()

# -----------------------------
# End of Reverse Row-wise Number Square Pattern
# -----------------------------
