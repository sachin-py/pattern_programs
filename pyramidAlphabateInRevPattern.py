'''
Right-Aligned Reversed Alphabet Triangle Pattern

Pattern for n = 5:

    E 
   E D
  E D C
 E D C B
E D C B A

Author : Sachin Kumar
GitHub : https://github.com/sachin-py/pattern_programs/
'''

n = 5

# Outer loop for each row
for i in range(n):
    # Print leading spaces for right alignment
    print(' ' * (n - i - 1), end='')

    # Inner loop to print characters from E downwards
    for j in range(i + 1):
        print(chr(64 + n - j), end=' ')

    # Newline after each row
    print()
