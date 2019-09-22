def kthSmallest(arr,n,k):
    arr_s = sorted(arr)
    return arr_s[k-1]
    
if __name__ == '__main__':
    T = int(input())
    for tc in range(T):
        N = int(input())
        arr = list(map(int,input().strip().split()))
        k = int(input())
        print (kthSmallest(arr,N,k))