{
#Initial Template for Python 3
import math
//Position this line where user code will be pasted.
    
def main():
    
    T=int(input())
    
    while(T>0):
        
        N=int(input())
        a=[int(x) for x in input().strip().split()]
        
        print(mean(a,N),median(a,N))
        
        T-=1
    
    
if __name__=="__main__":
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
##Complete the below codes
def median(A,N):
    
    A.sort()
    
    ##Your code here
    #If median is fraction then convert the median to integer and return
    if (N-1)%2 == 0:
        return (A[(N-1)//2])
    else:
        return (int((A[N//2 - 1] + A[N//2])/2))
    
def mean(A,N):
    ##Your code here
    total = sum(A)
    return (int(total/N))

