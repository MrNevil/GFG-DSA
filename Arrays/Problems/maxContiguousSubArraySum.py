{
#Initial Template for Python 3
import math
 
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            print(maxSubArraySum(arr,n))
            
            T-=1
if __name__ == "__main__":
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
##Complete this function
def maxSubArraySum(arr,size):
    ##Your code here
    indicator_array = [True if i >=0 else False for i in arr]
    if True in indicator_array:
        max_so_far=max_ending_here=0
        for a in range(size):
            max_ending_here = max_ending_here + arr[a]
            if max_ending_here < 0:
                max_ending_here = 0
            if max_so_far < max_ending_here:
                max_so_far = max_ending_here
        return (max_so_far)
    elif False in indicator_array and True not in indicator_array:
        return (max(arr))