'''
Diamond Shape Star Pattern

Pattern for n = 5:

    * 
   * *
  * * *
 * * * *
* * * * *
 * * * *
  * * *
   * *
    *

Author : Sachin Kumar
GitHub : https://github.com/sachin-py/pattern_programs/
'''

n = 5

# Upper pyramid
for i in range(n):
    print(' ' * (n - i - 1) + '* ' * (i + 1))

# Lower inverted pyramid
for j in range(n - 1):
    print(' ' * (j + 1) + '* ' * (n - j - 1))
