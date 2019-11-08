def checkRotation(s1,s2):
    if (s1[2:] + s1[:2] == s2) or (s1[-2:] + s1[:-2] == s2):
        return 1
    else:
        return 0

if __name__ == '__main__':
    t = int(input())
    for tcase in range(t):
        s1 = input()
        s2 = input()
        print (checkRotation(s1,s2))
        
        
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
        if(isRotated(s,p)):
            print(1)
        else:
            print(0)
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
'''
	Your task is to check if the given string can be obtained
	by rotating other string 'p' by two places.
	Function Arguments: s (given string), p(string to be rotated)
	Return Type: boolean
'''
def isRotated(s,p):
    #code here
    if (s[2:] + s[:2] == p) or (s[-2:] + s[:-2] == p):
        return 1
    else:
        return 0