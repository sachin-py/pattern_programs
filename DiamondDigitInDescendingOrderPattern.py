'''
Number Pyramid Pattern (Up and Down)

    5 
   5 4
  5 4 3
 5 4 3 2
5 4 3 2 1
 5 4 3 2
  5 4 3
   5 4
    5

Author : Sachin Kumar
GitHub : https://github.com/sachin-py/pattern_programs/
'''

n = 5

# Top half
for i in range(n):
    print(' ' * (n - i - 1), end='')
    for j in range(i + 1):
        print(n - j, end=' ')
    print()

# Bottom half
for i in range(n - 1):
    print(' ' * (i + 1), end='')
    for j in range(n - i - 1):
        print(n - j, end=' ')
    print()
