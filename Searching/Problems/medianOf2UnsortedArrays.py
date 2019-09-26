import math
def medianOf2Arrays(arr1,arr2,N,M):
    ar = arr1 + arr2
    ar = sorted(ar)
    if (N+M)%2 == 0:
        a = ar[((N+M)//2)-1]
        b = ar[((N+M)//2) + 1 - 1]
        return math.floor(((a+b)/2))
    else:
        c = ar[((N+M+1)//2)-1]
        return c
        
if __name__ == '__main__':
    t = int(input())
    for c in range(t):
        N,M = list(map(int,input().strip().split()))
        arr1 = list(map(int,input().strip().split()))
        arr2 = list(map(int,input().strip().split()))
        print (medianOf2Arrays(arr1,arr2,N,M))