{
#Initial Template for Python 3
import math
//Position this line where user code will be pasted.
    
def main():
    
    T=int(input())
    
    while(T>0):
        
        n=int(input())
        print(countSetBits(n))
        T-=1
if __name__=="__main__":
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
##Complete this function
def countSetBits(n):
    ##Your code here
    S = 0
    for i in range(1,n+1):
        bin_rep = bin(i)[2:]
        S += bin_rep.count('1')
    return (S)

