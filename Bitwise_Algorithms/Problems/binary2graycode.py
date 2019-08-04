{
#Initial Template for Python 3
import math
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        print(greyConverter(n))
        T-=1
if __name__=="__main__":
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
##Complete this fcuntion
def greyConverter(n):
    ##Your code here
    bin_rep = bin(n)[2:]
    gray = bin_rep[0]
    for i in range(1,len(bin_rep)):
        gray += str(int(bin_rep[i-1]) ^ int(bin_rep[i]))
    return int(gray,2)