{
#Initial Template for Python 3
import math
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        print(grayToBinary(n))
        T-=1
if __name__=="__main__":
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
##Complete this function
def grayToBinary(n):
    ##Your code here
    gray_rep = bin(n)[2:]
    binary = gray_rep[0]
    for i in range(1,len(gray_rep)):
        if gray_rep[i] == '0':
            binary += binary[i-1]
        else:
            binary += str(int(not int(binary[i-1])))
    return int(binary,2)