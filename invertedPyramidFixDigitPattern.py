'''
Number Inverted Pyramid Pattern with Indentation

Pattern for n = 5:

1 1 1 1 1 
 2 2 2 2
  3 3 3
   4 4
    5

Author : Sachin Kumar
GitHub : https://github.com/sachin-py/pattern_programs/
'''

n = 5

# Outer loop for each row
for i in range(n):
    # Print leading spaces for indentation
    print(' ' * i + (str(i + 1) + ' ') * (n - i))
