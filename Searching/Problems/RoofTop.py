{
#Initial Template for Python 3
import math
    
def main():
        T=int(input())
        while(T>0):
            
            N=int(input())
            A=[int(x) for x in input().strip().split()]
            
            print(maxStep(A,N))
            
            
            T-=1
if __name__ == "__main__":
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
#Complete this function
def maxStep(a,n):
    #Your code here
    all_steps = []
    steps = 0
    for i in range(1,n):
        if a[i-1] < a[i]:
            steps = max(steps,1)
            if i >= 2:
                if a[i-2] < a[i-1]:
                    steps += 1
        else:
            steps = 0
        all_steps.append(steps)
    if all_steps:
        return max(all_steps)
    else:
        return 0