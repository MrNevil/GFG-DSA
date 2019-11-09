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
        ans=nonrepeatingCharacter(s)
        if(ans!='$'):
            print(ans)
        else:
            print(-1)
            
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
'''
	Your task is to return the index of lefmost non-repeating 
	character or return
	-1 if all characters occur more than once.
	
	Function Arguments: s (given string)
	Return Type: integer
'''
def nonrepeatingCharacter(s):
    #code here
    import collections
    freqs = collections.Counter(s)
    if 1 not in freqs.values():
        return -1
    else:
        for c in s:
            if freqs[c]==1:
                return c