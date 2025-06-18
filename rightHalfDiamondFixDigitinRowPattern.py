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
'''

n = 5
for i in range(n):
    print((str(i+1)+' ')*(i+1))
for i in range(n-1):
    print((str(n-i-1)+' ')*(n-i-1))
