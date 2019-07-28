{
#Initial Template for Python 3
import math
//Position this line where user code will be pasted.
def main():
    
    T=int(input())
    
    while(T>0):
        
        N=int(input())
        
        if(isPrime(N)):
            print("Yes")
        else:
            print("No")
            
        
        T-=1
    
    
if __name__=="__main__":
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
##Complete this function
def isPrime(N):
    #Your code here
    if (N <= 1) : 
        return False
    if (N <= 3) : 
        return True
  
    # This is checked so that we can skip  
    # middle five numbers in below loop 
    if (N % 2 == 0 or N % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= N) : 
        if (N % i == 0 or N % (i + 2) == 0) : 
            return False
        i = i + 6
  
    return True
