{
#Initial Template for Python 3
import math
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        print(swapBits(n))
        T-=1
if __name__=="__main__":
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
##Complete this function
def swapBits(n):
    #Your code here
    even_bits = n & 0xAAAAAAAA
    odd_bits = n & 0x55555555
    even_bits >>= 1
    odd_bits <<= 1
    return (even_bits | odd_bits)