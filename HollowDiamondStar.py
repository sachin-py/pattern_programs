'''
Hollow Diamond Pattern Generator

Pattern for n = 4:

        * 
      *   *
    *       *
  *           *
*               *
  *           *
    *       *
      *   *
        *

Author : Sachin Kumar
GitHub : https://github.com/sachin-py/pattern_programs/
'''

# -----------------------------
# Hollow Diamond Pattern Logic
# -----------------------------

# Diamond height parameter (controls the top and bottom halves)
n = 5

# Upper half of the diamond (including the middle row)
for i in range(n):
    # Print leading spaces to center the star
    print('  ' * (n - i - 1) + '* ', end='')

    # Print spaces between the stars for hollow effect
    if i >= 1:
        print('  ' * (2 * i - 1) + '*', end='')
    print()  # Move to next line

# Lower half of the diamond
for i in range(n):
    if i != 0:
        print('  ' * i + '* ', end='')  # Print leading spaces

        # Print spaces between the stars for hollow effect
        if i != n - 1:
            print('  ' * (2 * n - 2 * i - 3) + '* ', end='')
        print()  # Move to next line

# -----------------------------
# End of Hollow Diamond Pattern
# -----------------------------
