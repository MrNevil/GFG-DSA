{
#Initial Template for Python 3
import math
def main():
        T=int(input())
        while(T>0):
            
            N=int(input())
            A=[int(x) for x in input().strip().split()]
            
            
            
            print(countOnes(A,N))
            
            T-=1
if __name__ == "__main__":
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
##Complete this code
def countOnes(A,N):
    #Your code here
    return A.count(1)