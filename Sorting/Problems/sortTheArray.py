def sort(arr,n):
    x = sorted(arr)
    return ' '.join(str(i) for i in x)
    
if __name__ == '__main__':
    T = int(input())
    for tcase in range(T):
        n = int(input())
        arr = list(map(int,input().strip().split()))
        print (sort(arr,n))