'''
Right-Aligned Number Triangle Pattern

Pattern for n = 5:

    1 
   2 2
  3 3 3
 4 4 4 4
5 5 5 5 5

Author : Sachin Kumar
GitHub : https://github.com/sachin-py/pattern_programs/
'''

n = 5

# -----------------------------
# Loop to print a right-aligned triangle with repeated numbers per row
# Leading spaces decrease as row number increases
# Each row prints the row number (i+1) repeated (i+1) times
# -----------------------------
for i in range(n):
    print(' ' * (n - i - 1) + (str(i + 1) + ' ') * (i + 1))

# -----------------------------
# End of Right-Aligned Number Triangle Pattern
# -----------------------------
