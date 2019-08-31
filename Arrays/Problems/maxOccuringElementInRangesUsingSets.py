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
    init = set(range(L[0],R[0]+1))
    for i in range(1,N):
        if set(range(L[i],R[i]+1)) & init != set():
            init = init & set(range(L[i],R[i]+1))
        else:
            continue
    return min(init)