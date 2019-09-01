{
#Initial Template for Python 3
import math
    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        N=int(input())
        
        A=[int(x) for x in input().strip().split()]
        
        A=leaders(A,N)
        
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
def leaders(A,N):
    #Your code here
    
    '''
    Just return the list with leaders in it
    '''
    leaders = []
    for i in range(N-1):
        X = A[i]
        Yarr = A[i+1:]
        a = max(Yarr)
        if a <= X:
            leaders.append(X)
    leaders.append(A[len(A)-1])
    return leaders