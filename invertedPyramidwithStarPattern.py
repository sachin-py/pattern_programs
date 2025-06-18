'''
Left-Aligned Inverted Pyramid Pattern

Pattern for n = 5:

* * * * * 
 * * * *
  * * *
   * *
    *

Author : Sachin Kumar
GitHub : https://github.com/sachin-py/pattern_programs/
'''

n = 5

# Outer loop for each row
for i in range(n):
    # Print leading spaces to shift the stars right
    print(' ' * i + '* ' * (n - i))
