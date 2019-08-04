{
#Initial Template for Python 3
import math
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        if isSparse(n):
            print("1")
        else:
            print("0")
        T-=1
if __name__=="__main__":
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
##Complete this function
def isSparse(n):
    #Your code here
    bin_rep = bin(n)[2:]
    k = bin_rep[0]
    for i in range(len(bin_rep[1:])):
        if k == '1':
            if bin_rep[1:][i] == k:
                return False
            else:
                k = bin_rep[1:][i]
        else:
            k = bin_rep[1:][i]
    return True