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
def maxAND(arr,n):
    #Your code here
    max_and = 0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if max_and <= (arr[i] & arr[j]):
                max_and = arr[i] & arr[j]
    return max_and