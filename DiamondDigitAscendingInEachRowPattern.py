'''
Number Pyramid Pattern (Up and Down)

Pattern for n = 5:

    1 
   1 2
  1 2 3
 1 2 3 4
1 2 3 4 5
 1 2 3 4
  1 2 3
   1 2
    1

Author : Sachin Kumar  
GitHub : https://github.com/sachin-py/pattern_programs/
'''

n = 5

# Top pyramid
for i in range(n):
    print(' ' * (n - i - 1), end='')
    for j in range(i + 1):
        print(j + 1, end=' ')
    print()

# Bottom inverted pyramid
for i in range(n - 1):
    print(' ' * (i + 1), end='')
    for j in range(n - i - 1):
        print(j + 1, end=' ')
    print()
