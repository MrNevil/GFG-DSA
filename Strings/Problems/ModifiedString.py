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
        s=str(input())
        print(modified(s))
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
'''
	Your task is to return minimum no of character
	to be inserted so that no three consecutive
	characters in the string are not same.
	
	Function Arguments: s (given string)
	Return Type: integer
'''
def modified(s):
    #code here
    import collections
    freqs = collections.Counter(s)
    S = 0
    for k,v in freqs.items():
        if v%3 == 0:
            S += (v//3)
        elif v < 3:
            S += 0
        elif v > 3 and v%3 != 0:
            S += (v%3)
    return S