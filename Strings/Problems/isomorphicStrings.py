{
#Initial Template for Python 3
import atexit
import io
import sys
from collections import defaultdict
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
        if(areIsomorphic(s,p)):
            print(1)
        else:
            print(0)
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
'''
	Your task is to check if the given strings are
	isomorphic or not.
	
	Function Arguments: s and p (given strings)
	Return Type: boolean
'''
def areIsomorphic(s,p):
    if len(s) != len(p):
        return False
    max_chars = 256
    marked = [False] * max_chars
    mapl = [-1] * max_chars
    for i in range(len(p)):
        if mapl[ord(s[i])] == -1:
            if marked[ord(p[i])] == True:
                return False
                
            marked[ord(p[i])] = True
            mapl[ord(s[i])] = p[i] 
            
        elif mapl[ord(s[i])] != p[i]: 
            return False
    return True