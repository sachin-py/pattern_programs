'''
Hollow Half Bottom Diamond Generator

Pattern for n = 6:

*                   *
  *               *
    *           *
      *       *
        *   *
          *

Author : Your Name
GitHub : https://github.com/yourusername/your-repo-name
'''

# -----------------------------
# Method 1: Compact Version
# -----------------------------

n = 6

for i in range(n):
    if i != n - 1:
        print('  ' * i + '* ' + '  ' * (2 * n - 2 * i - 3) + '* ')
    else:
        print('  ' * (n - 1) + '*')


# -----------------------------
# Method 2: Readable Version
# -----------------------------

for i in range(n):
    print('  ' * i + '* ', end='')
    if i != n - 1:
        print('  ' * (2 * n - 2 * i - 3) + '* ', end='')
    print()

# -----------------------------
# End of Hollow Inverted V Pattern
# -----------------------------
