{
#Initial Template for Python 3
import math
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        print(maxConsecutiveOnes(n))
        T-=1
if __name__=="__main__":
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
##Complete this function
def maxConsecutiveOnes(x):
    ##Your code here
    bin_rep = bin(x)[2:]
    str1s = bin_rep.split('0')
    #if the problem is about longest consecutive zeros
    #then 1 is used as delimiter/separator
    #str0s = bin_rep.split('1')
    return (max([len(u) for u in str1s]))