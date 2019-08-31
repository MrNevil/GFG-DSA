{
#Initial Template for Python 3
import math
def main():
    
    T=int(input())
    
    while(T>0):
        
        nk=[int(x) for x in input().strip().split()]
        
        N=nk[0]
        K=nk[1]
        
        A=[int(x) for x in input().strip().split()]
        
        A=reverseInGroups(A,N,K)
        
        for i in A:
            print(i,end=" ")
            
        print()
       
        T-=1
if __name__=="__main__":
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
#Complete this function
def reverseInGroups(A,N,K):
    #Your code here
    v = []
    for i in range(0,len(A),K):
        v += reversed(A[i:i+K])
    return v