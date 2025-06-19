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

This program prints a diamond shape using uppercase letters:
- The top half displays letters from A to the nth letter, centered with decreasing spaces.
- The bottom half mirrors the top, with decreasing letters and increasing spaces.

Author : Sachin Kumar
GitHub : https://github.com/sachin-py/pattern_programs/
'''

n = 5  # You can change this value to adjust the height

# Top half: letters increase, spaces decrease
for i in range(n):
    print('  ' * (n - i - 1) + (chr(65 + i) + ' ') * (i + 1))

# Bottom half: letters decrease, spaces increase
for i in range(n - 1):
    print('  ' * (i + 1) + (chr(64 + n - i - 1) + ' ') * (n - i - 1))
