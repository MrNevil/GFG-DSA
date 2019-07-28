{
#Initial Template for Python 3
import math
//Position this line where user code will be pasted.
def main():
    
    T=int(input())
    
    while(T>0):
        abc=[int(x) for x in input().strip().split()]
        a=abc[0]
        b=abc[1]
        c=abc[2]
        
        quadraticRoots(a,b,c)
        
        
        T-=1
    
    
if __name__=="__main__":
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
##Complete this function
def quadraticRoots(a,b,c):
    #Your code here
    D = (b*b)-(4*a*c)
    if D>=0:
        num1 = -1*b + math.sqrt(D)
        den = 2*a
        root1 = num1/den
        num2 = -1*b - math.sqrt(D)
        root2 = num2/den
        print (" ".join([str(max(root1,root2)),str(min(root1,root2))]))
    else:
        print ("Imaginary")
        