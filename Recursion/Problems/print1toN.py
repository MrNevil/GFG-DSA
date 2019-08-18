{
#Initial Template for Python 3
import math
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        N=int(input())
        
        printNos(N)
        print()
        T-=1
if __name__=="__main__":
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
#Complete this function
def printNos(N):
    #Your code here
    if N == 0:
        return
    else:
        printNos(N-1)
        print (N,end=" ")