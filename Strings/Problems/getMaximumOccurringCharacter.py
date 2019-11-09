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
        print(getMaxOccurringChar(s))
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
'''
	Your task is to return the lexicographically smallest 
	max occuring charcter in given string.
	
	Function Arguments: s (given string)
	Return Type: char or -1.
	
'''
def getMaxOccurringChar(s):
    #code here
    import collections
    freqs = collections.Counter(s)
    maxO = max(freqs.values())
    chars = []
    for c in s:
        if freqs[c] == maxO:
            chars.append(c)
    if len(chars) == 1:
        return chars[0]
    else:
        return min(chars)