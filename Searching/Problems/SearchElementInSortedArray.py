{
#Initial Template for Python 3
import math
def main():
        T=int(input())
        while(T>0):
            
            NK=(input().strip().split())
            N=int(NK[0])
            K=int(NK[1])
            
            A=[int(x) for x in input().strip().split()]
            
            
            
            print(searchInSorted(A,N,K))
            
            T-=1
if __name__ == "__main__":
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
##Complete this function
def searchInSorted(A,N,K):
    #Your code here
    if K in A:
        return (1)
    else:
        return (-1)