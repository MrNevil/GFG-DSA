{
#Initial Template for Python 3
import math
//Position this line where user code will be pasted.
    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        k=int(input())
        
        if checkKthBit(n,k):
            print("Yes")
        else:
            print("No")
        
        T-=1
if __name__=="__main__":
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
##Complete this code
def checkKthBit(n,k):
    #Your code here
    if (n & (1<<k)!=0):
        return True
    else:
        return False