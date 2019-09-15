{
#Initial Template for Python 3
import math
def main():
        T=int(input())
        while(T>0):
            
            N=int(input())
            A=[int(x) for x in input().strip().split()]
            
            x=int(input())
            
            print(leftIndex(N,A,x))
            
            
            T-=1
if __name__ == "__main__":
    main()
    
    
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
##Complete this function
def leftIndex(N,A,x):
    #Your code here
    l = 0
    r = N - 1
    def binarySearch(A,l,r,x):
        if x not in A:
            return -1
        mid = l + ((r-l)//2)
        if (A[mid]==x) & ((mid==0) | (A[mid-1]!=x)):
            return mid
        if A[mid] >= x:
            return binarySearch(A,l,mid-1,x)
        if A[mid] < x:
            return binarySearch(A,mid+1,r,x)
    ans = binarySearch(A,l,r,x)
    return ans