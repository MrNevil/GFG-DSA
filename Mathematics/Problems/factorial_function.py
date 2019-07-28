{
#Initial Template for Python 3
import math
//Position this line where user code will be pasted.
def main():
    
    T=int(input())
    
    while(T>0):
        N=int(input())
        
        print(factorial(N))
        
        
        T-=1
    
    
if __name__=="__main__":
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
##You need to complete this function
def factorial(N):
    ##Your code here
    if N==0:
        return 1
    else:
        return (N*factorial(N-1))