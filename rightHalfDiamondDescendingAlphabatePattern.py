'''
E 
E D
E D C
E D C B
E D C B A
E D C B
E D C
E D
E

This program prints an inverted alphabetical pyramid:
- The first half prints characters from 'E' down to a decreasing letter on each new line.
- The second half mirrors the first half, reducing the number of characters line by line.

Author : Sachin Kumar
GitHub : https://github.com/sachin-py/pattern_programs/
'''

n = 5

# Upper half: Print from 'E' down to (E - i) for each row
for i in range(n):
    for j in range(i + 1):
        print(chr(64 + n - j), end=' ')
    print()

# Lower half: Mirror the pattern by reducing characters per row
for i in range(n - 1):
    for j in range(n - i - 1):
        print(chr(64 + n - j), end=' ')
    print()
