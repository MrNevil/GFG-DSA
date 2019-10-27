def ifArraysEqual(arr1,arr2):
    if set(arr1)==set(arr2):
        return 1
    else:
        return 0
        
if __name__ == '__main__':
    t = int(input())
    for tcase in range(t):
        N = int(input())
        arr1 = list(map(int,input().strip().split()))
        arr2 = list(map(int,input().strip().split()))
        print (ifArraysEqual(arr1,arr2))