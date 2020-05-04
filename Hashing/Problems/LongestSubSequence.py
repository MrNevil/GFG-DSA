# Copied from geeksforgeeks
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
if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        n=int(input())
        a = list(map(int, input().strip().split()))
        print(findLongestConseqSubseq(a,n))
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
'''
	Your task is to return the length of longest subsequence
	with consecutive elements present( order does not matter).
	
	Function Arguments: array a with size n. 
	Return Type: Integer
'''
def findLongestConseqSubseq(a,n):
    #code here
    s = set() 
    ans=0
    for ele in a: 
        s.add(ele) 

    for i in range(n): 
        if (a[i]-1) not in s: 
            j=a[i] 
            while(j in s): 
                j+=1
            ans=max(ans, j-a[i]) 
    return ans
