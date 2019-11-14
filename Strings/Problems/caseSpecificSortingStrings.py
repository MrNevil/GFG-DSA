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
        s=str(input())
        print(caseSort(s,n))
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
'''
	Your task is to return the case sorted string
	as described in the problem statement above.
	
	Function Arguments: string s and size n. 
	Return Type: string
'''
def caseSort(s,n):
    #code here
    upper_chars = sorted([i for i in s if i.isupper()])
    lower_chars = sorted([i for i in s if i.islower()])
    sorted_string = []
    for c in s:
        if c.islower():
            sorted_string.append(lower_chars[0])
            x = lower_chars.pop(0)
        elif c.isupper():
            sorted_string.append(upper_chars[0])
            x = upper_chars.pop(0)
    return ''.join(sorted_string)