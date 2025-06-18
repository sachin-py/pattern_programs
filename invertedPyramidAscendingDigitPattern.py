'''
Inverted Number Pyramid with Indentation

Pattern for n = 5:

1 2 3 4 5 
 1 2 3 4
  1 2 3
   1 2
    1

Author : Sachin Kumar
GitHub : https://github.com/sachin-py/pattern_programs/
'''

n = 5

# Outer loop for each row
for i in range(n):
    # Print leading spaces for indentation
    print(' ' * i, end='')
    # Print numbers from 1 to (n - i)
    for j in range(n - i):
        print(j + 1, end=' ')
    print()
