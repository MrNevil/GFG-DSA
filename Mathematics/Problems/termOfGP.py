{
#Initial Template for Python 3
import math
//Position this line where user code will be pasted.
def main():
    
    T=int(input())
    
    while(T>0):
        
        AB=[int(x) for x in input().strip().split()]
        A=AB[0]
        B=AB[1]
        
        N=int(input())
        
        print(math.floor(termOfGP(A,B,N)))
        
        T-=1
    
    
if __name__=="__main__":
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
#Compelte his function
def termOfGP(A,B,N):
    #Your code here
    return (A*((B/A)**(N-1)))
