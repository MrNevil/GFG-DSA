{
#Initial Template for Python 3
import math
A=[0]*1000000
            
def main():
    
    T=int(input())
    
    while(T>0):
        
        global A
        A=[0]*1000000
        
        N=int(input())
        
        L=[int(x) for x in input().strip().split()]
        R=[int(x) for x in input().strip().split()]
        
        maxx=max(R)
        
        print(maxOccured(L,R,N,maxx))
            
        
       
        T-=1
if __name__=="__main__":
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
#Complete this function
def maxOccured(L,R,N,maxx):
    ##Your code here
    MAX = 50000
    arr = [0 for i in range(MAX)]
    for i in range(0, N, 1): 
        arr[L[i]] += 1
        arr[R[i] + 1] -= 1
    msum = arr[0] 
    for i in range(1, MAX, 1): 
        arr[i] += arr[i - 1] 
        if (msum < arr[i]): 
            msum = arr[i] 
            ind = i 
    return ind