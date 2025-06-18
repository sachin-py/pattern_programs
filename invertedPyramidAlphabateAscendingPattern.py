'''
Inverted Alphabet Pyramid with Indentation

Pattern for n = 6:

A B C D E F 
 A B C D E
  A B C D
   A B C
    A B
     A

Author : Sachin Kumar
GitHub : https://github.com/sachin-py/pattern_programs/
'''

n = 6

# Outer loop for each row
for i in range(n):
    # Print leading spaces for indentation
    print(' ' * i, end='')
    # Print characters from 'A' to appropriate limit
    for j in range(n - i):
        print(chr(65 + j), end=' ')
    print()
