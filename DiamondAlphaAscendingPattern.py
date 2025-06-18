'''
Alphabet Pyramid Pattern (Up and Down)

Pattern for n = 5:

    A 
   A B
  A B C
 A B C D
A B C D E
 A B C D
  A B C
   A B
    A

Author : Sachin Kumar  
GitHub : https://github.com/sachin-py/pattern_programs/
'''

n = 5

# Top half of the pyramid
for i in range(n):
    print(' ' * (n - i - 1), end='')
    for j in range(i + 1):
        print(chr(65 + j), end=' ')
    print()

# Bottom half of the pyramid
for i in range(n - 1):
    print(' ' * (i + 1), end='')
    for j in range(n - i - 1):
        print(chr(65 + j), end=' ')
    print()
