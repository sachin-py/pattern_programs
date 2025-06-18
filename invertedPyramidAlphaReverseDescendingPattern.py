'''
Indented Reverse Alphabet Pattern (Starting from 'E')

Pattern for n = 5:

E D C B A 
 E D C B
  E D C
   E D
    E

Author : Sachin Kumar
GitHub : https://github.com/sachin-py/pattern_programs/
'''

n = 5

# Outer loop for each row
for i in range(n):
    # Print leading spaces for indentation
    print(' ' * i, end='')
    # Print characters from E downwards, reducing in each row
    for j in range(n - i):
        print(chr(64 + n - j), end=' ')
    print()
