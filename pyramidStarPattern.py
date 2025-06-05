'''
Right-Angled Triangle Star Pattern (Aligned Right)

Pattern example for n = 4:

   * 
  * *
 * * *
* * * *

Author : Sachin Kumar
GitHub : https://github.com/sachin-py/pattern_programs/
'''

n = 4

# -----------------------------
# Loop to print right-aligned triangle of stars increasing each row
# Spaces decrease and stars increase per row
# -----------------------------
for i in range(n):
    print(' ' * (n - i - 1) + '* ' * (i + 1))

# -----------------------------
# End of Right-Angled Triangle Star Pattern
# -----------------------------
