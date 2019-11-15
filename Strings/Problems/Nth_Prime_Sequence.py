def NthPrime(n):
    nums = ""
    while (n > 0):
        rem = n%4
        if rem == 1:
            nums += '2'
        if rem == 2:
            nums += '3' 
        if rem == 3:
            nums += '5'
        if rem == 0:
            n -= 1
            nums += '7'
        n = n//4
    return nums[::-1]

if __name__ == '__main__':
    t = int(input())
    for tcase in range(t):
        n = int(input())
        print (NthPrime(n))