{
#Initial Template for Python 3
import math
    
def main():
        T=int(input())
        while(T>0):
            
            N=int(input())
            
            A=[int(x) for x in input().strip().split()]
            
            x=int(input())
            
            print(search(A,N,x))
            
            T-=1
if __name__ == "__main__":
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
#Complete the below function
def search(A,N,x):
    #Your code here
    if x in A:
        return A.index(x)
    else:
        return -1