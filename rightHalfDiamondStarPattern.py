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

This program prints a star (*) pyramid:
- The first half increases from 1 to n stars per line.
- The second half mirrors the first half in reverse, decreasing to 1 star.

Author : Sachin Kumar
GitHub : https://github.com/sachin-py/pattern_programs/
'''

n = 5

# Upper half: increasing number of stars
for i in range(n):
    print('* ' * (i + 1))

# Lower half: decreasing number of stars
for i in range(n - 1):
    print('* ' * (n - i - 1))
