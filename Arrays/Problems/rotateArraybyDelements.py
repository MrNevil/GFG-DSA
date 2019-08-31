{
#Initial Template for Python 3
import math
def main():
    
    T=int(input())
    
    while(T>0):
        
        nd=[int(x) for x in input().strip().split()]
        
        N=nd[0]
        D=nd[1]
        
        A=[int(x) for x in input().strip().split()]
        
        rotateArr(A,D,N)
        
        for i in A:
            print(i,end=" ")
            
        print()
       
        T-=1
if __name__=="__main__":
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
##Complete this functiom
def rotateArr(A,D,N):
    ##Your code here
    A[:D] = A[:D][::-1]
    A[D:] = A[D:][::-1]
    f = A[:D] + A[D:]
    A[:] = f[::-1]