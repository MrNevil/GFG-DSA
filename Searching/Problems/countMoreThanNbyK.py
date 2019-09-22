{
#Initial Template for Python 3
import math
def main():
        T=int(input())
        while(T>0):
            
            N=int(input())
            A=list(map(int,input().split()))
            
            K=int(input())
            
            print(countOccurence(A, N, K))
            
            
            T-=1
if __name__ == "__main__":
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
#Complete this function
def countOccurence(arr,n,k):
    #Your code here
    import collections
    freqs = collections.Counter(arr)
    c = 0
    for u,v in freqs.items():
        if v > n/k:
            c += 1
    return c