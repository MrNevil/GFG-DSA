{
#Initial Template for Python 3
import math
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        ab=[int(x) for x in input().strip().split()]
        a=ab[0]
        b=ab[1]
        print(countBitsFlip(a,b))
        T-=1
if __name__=="__main__":
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
##Complete this function
def countBitsFlip(a,b):
    ##Your code here
    c = a ^ b
    cc = bin(c)[2:].count('1')
    return (cc)
