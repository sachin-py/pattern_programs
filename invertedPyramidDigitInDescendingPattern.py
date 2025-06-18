'''
Indented Reverse Number Pattern

Pattern for n = 5:

5 4 3 2 1 
 5 4 3 2
  5 4 3
   5 4
    5

Author : Sachin Kumar
GitHub : https://github.com/sachin-py/pattern_programs/
'''

n = 5

# Outer loop for each row
for i in range(n):
    # Print indentation spaces
    print(' ' * i, end='')
    # Print decreasing numbers from 5
    for j in range(n - i):
        print(n - j, end=' ')
    print()
