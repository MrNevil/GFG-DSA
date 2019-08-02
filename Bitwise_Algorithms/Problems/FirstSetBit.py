{
#Initial Template for Python 3
import math
//Position this line where user code will be pasted.
    
    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        
        print(getFirstSetBit(n))
        
        
        T-=1
    
    
if __name__=="__main__":
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
##Complete this function
def getFirstSetBit(n):
    #Your code here
    bin_rep = bin(n)
    req_bin_rep = bin_rep[1:][::-1]
    if '1' not in req_bin_rep:
        return "0"
    else:
        for ind,val in enumerate(req_bin_rep):
            if val == '1':
                break
        return (ind+1)