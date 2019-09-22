## Available in GeeksForGeeks ##
{
#Initial Template for Python 3
import math
    
def main():
        T=int(input())
        while(T>0):
            
            N=int(input())
            A=[int(x) for x in input().strip().split()]
            
            twoRepeated(A,N)
            print()
            
            T-=1
if __name__ == "__main__":
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
##Complete this code
def twoRepeated(arr,n):
    #Your code here
    count = [0] * (n+2)
    for i in range(0, n+2) : 
        if(count[arr[i]] == 1) : 
            print(arr[i], end = " ") 
        else : 
            count[arr[i]] = count[arr[i]] + 1
