{
#Initial Template for Python 3
import math
def main():
    
    T=int(input())
    
    while(T>0):
        
        N=input()
        R=N[::-1]
        
        
        ans=power(int(N),int(R))
        print(ans)
        
        T-=1
if __name__=="__main__":
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
#Complete this function
def power(N,R):
    #Your code here
    return (pow(N,R)%1000000007)