#### solution using set data structure in python
# No hashing needed

def union(arr1,arr2):
    return len(set(arr1).union(set(arr2)))
    
if __name__ == '__main__':
    t = int(input())
    for case in range(t):
        m,n = list(map(int,input().strip().split()))
        arr1 = list(map(int,input().strip().split()))
        arr2 = list(map(int,input().strip().split()))
        print (union(arr1,arr2))