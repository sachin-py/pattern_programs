'''
Alphabet Pyramid Pattern (Up and Down)

Pattern for n = 5:

    A 
   B B
  C C C
 D D D D
E E E E E
 D D D D
  C C C
   B B
    A

Author : Sachin Kumar  
GitHub : https://github.com/sachin-py/pattern_programs/
'''

n = 5

# Top pyramid
for i in range(n):
    print(' ' * (n - i - 1) + (chr(65 + i) + ' ') * (i + 1))

# Bottom inverted pyramid
for i in range(n - 1):
    print(' ' * (i + 1) + (chr(64 + n - i - 1) + ' ') * (n - i - 1))
