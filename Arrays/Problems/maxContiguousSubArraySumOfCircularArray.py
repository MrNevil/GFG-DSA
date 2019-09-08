{
#Initial Template for Python 3
import math
    
    
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            print(circularSubarraySum(arr,n))
            
            T-=1
if __name__ == "__main__":
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
#Complete this function
def maxSubArraySum(arr):
    ##Your code here
    indicator_array = [True if i >=0 else False for i in arr]
    if True in indicator_array:
        max_so_far=max_ending_here=0
        for a in range(len(arr)):
            max_ending_here = max_ending_here + arr[a]
            if max_ending_here < 0:
                max_ending_here = 0
            if max_so_far < max_ending_here:
                max_so_far = max_ending_here
        return (max_so_far)
    elif False in indicator_array and True not in indicator_array:
        return (max(arr))
        
        
def circularSubarraySum(arr,n):
    indicator_array = [True if i >=0 else False for i in arr]
    ##Your code here
    # Case 1: get the maximum sum using standard kadane's 
    # algorithm 
    if True in indicator_array:
        max_kadane = maxSubArraySum(arr) 
  
        # Case 2: Now find the maximum sum that includes corner 
        # elements. 
        max_wrap = 0
        for i in range(0,n):
            max_wrap += arr[i] 
            arr[i] = -arr[i] 
 
        # Max sum with corner elements will be: 
        # array-sum - (-max subarray sum of inverted array) 
        max_wrap = max_wrap + maxSubArraySum(arr) 
  
        # The maximum circular sum will be maximum of two sums 
        if max_wrap > max_kadane: 
            return max_wrap 
        else: 
            return max_kadane
    elif False in indicator_array and True not in indicator_array:
        return (max(arr))