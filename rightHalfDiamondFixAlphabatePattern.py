'''
A 
B B
C C C
D D D D
E E E E E
D D D D
C C C
B B
A

This program prints an alphabetical pyramid:
- The first half prints letters from A to the nth letter, with each row repeating the letter.
- The second half mirrors the top in reverse, going back to A.

Author : Sachin Kumar
GitHub : https://github.com/sachin-py/pattern_programs/
'''

n = 5

# Upper half: increasing letters from A onward
for i in range(n):
    # Print character starting from 'A', repeated i+1 times
    print((chr(65 + i) + ' ') * (i + 1))

# Lower half: decreasing letters from second-last line back to 'A'
for i in range(n - 1):
    # Print character from 'E' down to 'B', repeated (n - i - 1) times
    print((chr(64 + n - i - 1) + ' ') * (n - i - 1))
