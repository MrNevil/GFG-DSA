import math
def isPowerOf2(N):
    if N==0:
        return "NO"
    if str(math.log2(N)).split('.')[1] == '0':
        return "YES"
    else:
        return "NO"
    
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        print (isPowerOf2(N))