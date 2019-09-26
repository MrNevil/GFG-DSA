# Naive Solution O(n*n) #
{
#Initial Template for Python 3
import math
def main():
        T=int(input())
        while(T>0):
            
            NS=input().strip().split()
            N=int(NS[0])
            S=int(NS[1])
            
            A=list(map(int,input().split()))
            
            subArraySum(A, N, S)
            
            print()
            
            T-=1
if __name__ == "__main__":
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
#Complete this function
def subArraySum(arr, n, s): 
    #Your code here
    flag = []
    for i in range(n):
        for j in range(i+1,n):
            if sum(arr[i:j+1]) == s:
                print (" ".join([str(i+1),str(j+1)]),end="")
                flag.append(1)
                return
    if not flag:
        print (-1,end="")
        return
