n = 4


for i in range(n):
    for a in range(n-i-1):
        print(" ", end='')
    for b in range(2*i+1):
        print('*', end='')
    print()
