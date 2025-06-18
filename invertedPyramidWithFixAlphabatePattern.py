'''
Alphabet Inverted Pyramid Pattern with Indentation

Pattern for n = 5:

A A A A A 
 B B B B
  C C C
   D D
    E

Author : Sachin Kumar
GitHub : https://github.com/sachin-py/pattern_programs/
'''

n = 5

# Outer loop for each row
for i in range(n):
    # Print leading spaces for indentation and characters in each row
    print(' ' * i + (chr(65 + i) + ' ') * (n - i))
