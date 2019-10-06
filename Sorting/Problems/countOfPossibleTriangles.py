# Refer geeksforgeeks for this solution #
{
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
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        size = int(input())
        arr = list(map(int, input().strip().split()))
        print(findNumberOfTriangles(arr,size))

}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
''' Your task is to return the total no of triangles possible.'''
def findNumberOfTriangles(arr,n):
    #code here
    if n < 3:
        return 0
    a = sorted(arr)
    count = 0
    for i in range(n - 1, 0, -1): 
        l = 0; 
        r = i - 1; 
        while(l < r): 
            if(a[l] + a[r] > a[i]): 
  
                # If it is possible with a[l], a[r] 
                # and a[i] then it is also possible 
                # with a[l+1]..a[r-1],a[r] and a[i] 
                count += r - l;  
  
                # checking for more possible solutions 
                r -= 1;  
              
            else: 
  
                # if not possible check for  
                # higher values of arr[l] 
                l += 1;
    return count
