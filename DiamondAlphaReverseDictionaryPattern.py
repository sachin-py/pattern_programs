'''
Pyramid of Descending Letters (Up and Down)

    E 
   E D
  E D C
 E D C B
E D C B A
 E D C B
  E D C
   E D
    E

Author : Sachin Kumar
GitHub : https://github.com/sachin-py/pattern_programs/
'''

n = 5

# Top half
for i in range(n):
    print(' ' * (n - i - 1), end='')
    for j in range(i + 1):
        print(chr(64 + n - j), end=' ')
    print()

# Bottom half
for i in range(n - 1):
    print(' ' * (i + 1), end='')
    for j in range(n - i - 1):
        print(chr(64 + n - j), end=' ')
    print()
