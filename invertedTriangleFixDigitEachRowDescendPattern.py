'''
Inverted Number Repetition Pattern (Descending Values)

Pattern for n = 5:

5 5 5 5 5 
4 4 4 4
3 3 3
2 2
1

Author : Sachin Kumar
GitHub : https://github.com/sachin-py/pattern_programs/
'''

n = 5

# -----------------------------
# Loop to print decreasing repetitions of descending numbers from n to 1
# -----------------------------
for i in range(n):
    print((str(n - i) + ' ') * (n - i))

# -----------------------------
# End of Inverted Number Repetition Pattern
# -----------------------------
