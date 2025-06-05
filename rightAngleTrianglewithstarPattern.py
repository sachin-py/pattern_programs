'''
Right-Angled Triangle Star Pattern Generator

Pattern for n = 4:

* 
* * 
* * * 
* * * * 

Author : Sachin Kumar
GitHub : https://github.com/sachin-py/pattern_programs/
'''

# -----------------------------
# Method 1: Using string multiplication
# -----------------------------

n = 4

for i in range(n):
    print(('* ') * (i + 1))


# -----------------------------
# Method 2: Using nested loops
# -----------------------------

print('Alternate\n')

for i in range(n):
    for j in range(i + 1):
        print('*', end=' ')
    print()

# -----------------------------
# End of Right-Angled Triangle Star Pattern
# -----------------------------
