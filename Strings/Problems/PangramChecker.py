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
        if(checkPanagram(s)):
            print(1)
        else:
            print(0)
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
''' Your task is to check if the given string is
	a panagram or not.
	
	Function Arguments: s (given string)
	Return Type: boolean
'''
def checkPanagram(s):
    #code here
    import string
    letters = set(string.ascii_lowercase)
    gletters = set(s)
    if gletters & letters == letters:
        return True
    else:
        return False