def maxCollectiveAbility(arr,n):
    new_arr = sorted(arr)
    prod1 = new_arr[n-3] * new_arr[n-2] * new_arr[n-1]
    prod2 = new_arr[0] * new_arr[1] * new_arr[n-1]
    return max(prod1,prod2)
    
if __name__ == '__main__':
    T = int(input())
    for tcase in range(T):
        N = int(input())
        arr = list(map(int,input().strip().split()))
        print (maxCollectiveAbility(arr,N))