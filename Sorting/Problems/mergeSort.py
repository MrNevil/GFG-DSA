{
#Initial Template for Python 3
if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        mergeSort(arr)
        for i in range(n):
            print(arr[i],end=" ")
        print()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3

def merge(arr, l, m, r): 
    n1 = m - l + 1
    n2 = r- m 
    # create temp arrays 
    L = [0] * (n1) 
    R = [0] * (n2) 
    # Copy data to temp arrays L[] and R[] 
    for i in range(0 , n1): 
        L[i] = arr[l + i] 
    for j in range(0 , n2): 
        R[j] = arr[m + 1 + j] 
    # Merge the temp arrays back into arr[l..r] 
    i = 0     # Initial index of first subarray 
    j = 0     # Initial index of second subarray 
    k = l     # Initial index of merged subarray 
    while i < n1 and j < n2 : 
        if L[i] <= R[j]: 
            arr[k] = L[i] 
            i += 1
        else: 
            arr[k] = R[j] 
            j += 1
        k += 1
    # Copy the remaining elements of L[], if there 
    # are any 
    while i < n1: 
        arr[k] = L[i] 
        i += 1
        k += 1
    # Copy the remaining elements of R[], if there 
    # are any 
    while j < n2: 
        arr[k] = R[j] 
        j += 1
        k += 1
        
def mergeSort(arr):
    #add code here
    start=0
    end = len(arr)-1
    ms(arr,start,end)
    
def ms(arr,start,end):
    if (start < end):
        mid = (start + end - 1)//2
        ms(arr,start,mid)
        ms(arr,mid+1,end)
        merge(arr,start,mid,end)