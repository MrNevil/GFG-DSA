{
#Initial Template for Python 3
import math
from sys import stdin
def main():
        T=int(input())
        while(T>0):
            
            N=int(input())
            A=[int(x) for x in input().strip().split()]
            
            
            
            print(majorityElement(A,N))
            
            T-=1
if __name__ == "__main__":
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
#Complete this function
def majorityElement(A,N):
    #Your code here
    import collections
    freqs = collections.Counter(A)
    for k,v in freqs.items():
        if v > N/2:
            return k
    return -1