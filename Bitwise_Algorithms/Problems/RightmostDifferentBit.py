{
#Initial Template for Python 3
import math
def getRightMostSetBit(n):
    return math.log2(n&-n)+1
    //Position this line where user code will be pasted.
    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        mn=[int(x) for x in input().strip().split()]
        m=mn[0]
        n=mn[1]
        
        print(math.floor(posOfRightMostDiffBit(m,n)))
        
        
        
        
        T-=1
    
    
if __name__=="__main__":
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
##Complete this function
def posOfRightMostDiffBit(m,n):
    #Your code here
    if m==n:
        return -1
    else:
        num = ~(m^n)
        k = 1
        while True:
            if (num & (1<<(k-1)))==0:
                return k
            else:
                k += 1