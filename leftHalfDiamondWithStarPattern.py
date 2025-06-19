'''
        * 
      * *
    * * *
  * * * *
* * * * *
  * * * *
    * * *
      * *
        *

This program prints a centered diamond made of stars:
- The top half is a left-aligned pyramid using increasing stars and decreasing spaces.
- The bottom half mirrors the top half, reducing stars and increasing spaces.

Author : Sachin Kumar
GitHub : https://github.com/sachin-py/pattern_programs/
'''

n = 5

# Upper half: increasing stars with decreasing leading spaces
for i in range(n):
    print('  ' * (n - i - 1) + '* ' * (i + 1))

# Lower half: decreasing stars with increasing leading spaces
for i in range(n - 1):
    print('  ' * (i + 1) + '* ' * (n - i - 1))
