{
#Initial Template for Python 3
import math
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        
        arr=[int(x) for x in input().strip().split()]
        
        print(maxAND(arr,n))
        T-=1
if __name__=="__main__":
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
#Complete this function
def checkBit(pattern,arr,  n) : 
    count = 0
      
    for i in range(0, n) : 
        if ((pattern & arr[i]) == pattern) : 
            count = count + 1
    return count 
  
# Function for finding maximum and  
# value pair 
def maxAND (arr,  n) : 
    res = 0
      
    # iterate over total of 30bits  
    # from msb to lsb 
    for bit in range(31,-1,-1) : 
        
        # find the count of element 
        # having set  msb 
        count = checkBit(res | (1 << bit), arr, n) 
   
        # if count >= 2 set particular 
        # bit in result 
        if ( count >= 2 ) : 
            res =res | (1 << bit) 
              
    return res