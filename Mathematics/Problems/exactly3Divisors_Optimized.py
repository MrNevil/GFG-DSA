{
#Initial Template for Python 3
import math
//Position this line where user code will be pasted.
def main():
    
    T=int(input())
    
    while(T>0):
        
        N=int(input())
        
        print(exactly3Divisors(N))
        
        T-=1
    
if __name__=="__main__":
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
##Complete this function
def exactly3Divisors(N):
    count = 0
    i = 2
    while ((i*i)<=N):
        flag=True
        j = 2
        while (j <= i/2):
            if i%j == 0:
                flag = False
            j += 1
            
        if flag:
            count += 1
        i += 1
    return (count)