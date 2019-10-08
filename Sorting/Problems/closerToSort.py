{
#Initial Template for Python 3
import math
    
def main():
        T=int(input())
        while(T>0):
            N=int(input())
            A=list(map(int,input().split()))
            X=int(input())
            res=closer(A,N,X)
            print(res)
            T-=1
if __name__ == "__main__":
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
##Complete this function
def closer( arr, n,  x):
    #Your code here
    if x in arr:
        return arr.index(x)
    else:
        return -1