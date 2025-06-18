'''
Number Pyramid Pattern (Up and Down)

Pattern for n = 6:

     1 
    2 2
   3 3 3
  4 4 4 4
 5 5 5 5 5
6 6 6 6 6 6
 5 5 5 5 5
  4 4 4 4
   3 3 3
    2 2
     1

Author : Sachin Kumar
GitHub : https://github.com/sachin-py/pattern_programs/
'''

n = 6

# Top pyramid
for i in range(n):
    print(' ' * (n - i - 1) + (str(i + 1) + ' ') * (i + 1))

# Bottom inverted pyramid
for i in range(n - 1):
    print(' ' * (i + 1) + (str(n - i - 1) + ' ') * (n - i - 1))
