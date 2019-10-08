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
        n,m = map(int, input().strip().split())
        a = list(map(int, input().strip().split()))
        b = list(map(int, input().strip().split()))
        merge(a,n,b,m)
        if(len(a)!=n and len(b)!=m):
            print("Do in O(1) space")
        print(*a,end=" ")
        print(*b)
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
'''
	Your task is to merge two sorted arrays in one 
	without using extra space.
	
	Function Arguments: array a with size n and array b with size m.
	Return Type: none,just modify the two arrays accordingly..
	the main function prints the arrays as follows:
	
	{
	    print(*a,end=" ")
        print(*b)
	}
'''
def merge(a,n,b,m):
    #code here
    x = sorted(a+b)
    a[:n] = x[:n]
    b[:m] = x[n:n+m]