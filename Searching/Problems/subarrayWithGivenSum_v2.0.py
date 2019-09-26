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
    curr_sum=0
    j=0
    for i in range(n):
        curr_sum += arr[i]
        while curr_sum > s:
            curr_sum -= arr[j]
            j += 1
        if curr_sum == s:
            print (" ".join([str(j+1),str(i+1)]),end="")
            break
    if curr_sum != s:
        print (-1,end="")