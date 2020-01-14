#User function Template for python3
'''
Function Arguments :
		@param  : histogram( given list containing info about histogram)
		@return : integer
'''

def getMaxArea(histogram):
    #code here
    n = len(histogram)
    stack = []
    maxArea = 0
    i = 0
    while (i < n):
        if ((len(stack)==0) or (histogram[i] >= histogram[stack[-1]])):
            stack.append(i)
            i += 1
        else:
            x = histogram[stack.pop()]
            temp = 0
            if len(stack) == 0:
                temp = x*i
            else:
                temp = x*(i-stack[-1]-1)
            if temp > maxArea:
                maxArea = temp
    while (len(stack) != 0):
        temp = 0
        x = stack.pop()
        if len(stack) == 0:
            temp = histogram[x] * n
        else:
            temp = histogram[x] * (n-stack[-1]-1)
        if temp > maxArea:
            maxArea = temp
    return maxArea


#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

# This code is contributed  
# by Jinay Shah 

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        print(getMaxArea(a))
# } Driver Code Ends