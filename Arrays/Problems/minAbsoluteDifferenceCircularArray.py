{
#Initial Template for Python 3
def main():
    T=int(input())
    while(T>0):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        
       
        
        print(minAdjDiff(arr,n))
        
        T-=1
if __name__=="__main__":
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
#Complete this function
def minAdjDiff(arr, n):
    ##Your code here
    min_dff = abs(arr[0]-arr[1])
    for i in range(1,len(arr)-1):
        if abs(arr[i]-arr[i+1]) < min_dff:
            min_dff = abs(arr[i]-arr[i+1])
        else:
            continue
    if min_dff > abs(arr[0]-arr[n-1]):
        min_dff = abs(arr[0]-arr[n-1])
    return min_dff