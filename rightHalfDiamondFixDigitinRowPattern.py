'''
1 
2 2
3 3 3
4 4 4 4
5 5 5 5 5
4 4 4 4
3 3 3
2 2
1

This program prints a pyramid pattern of numbers:
- The upper half increases from 1 to n, with each number repeated on its line.
- The lower half is a mirror of the upper half in reverse.
'''

# Author : Sachin Kumar
# GitHub : https://github.com/sachin-py/pattern_programs/

n = 5

# Upper half of the pattern (1 to n)
for i in range(n):
    # Print the number (i+1), repeated (i+1) times with space
    print((str(i+1) + ' ') * (i+1))

# Lower half of the pattern (n-1 to 1)
for i in range(n-1):
    # Print the number (n - i - 1), repeated that many times
    print((str(n - i - 1) + ' ') * (n - i - 1))
