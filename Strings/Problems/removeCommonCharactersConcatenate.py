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
        p=str(input())
        print(concatenatedString(s,p))
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
'''
	Your task is to return concatenated string
	after removing characters which are
	common to both string.
	
	Function Arguments: s and p (given strings)
	Return Type: string
'''
def concatenatedString(s,p):
    #code here
    cms = set(s) & set(p)
    rst = []
    for i in s:
        if i not in cms:
            rst.append(i)
    for i in p:
        if i not in cms:
            rst.append(i)
    if len(rst) == 0:
        return -1
    else:
        return ''.join(rst)