def setbits(n):
    x = bin(n)[2:]
    return x.count('1')

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        print (setbits(N))