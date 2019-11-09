{
# Initial Template for Python 3
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
    for i in range(t):
        s = str(input())
        s = reverseWords(s)
        print()

}
''' This is a function problem.You only need to complete the function given below '''
# User function Template for python3
'''
	Your task is to reverse the string without reversing
	individual words and return the obtained string.
	Function Arguments: s (given string)
	Return Type: string
'''
def reverseWords(s):
    # code here
    tokens = s.split('.')
    rtokens = tokens[::-1]
    print ('.'.join(rtokens),end='')