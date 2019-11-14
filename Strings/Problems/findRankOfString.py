{
#Initial Template for Python 3
#Contributed by : Nagendra Jha
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
    for tt in range(t):
        s=str(input())
        print(findRank(s))

}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
'''
	Your task is to return the rank of the given string,
	or return 0 if repeated characters are found.
	
	Function Arguments: string s.
	Return Type: Integer
'''
def findRank(s):
    #code here
    import itertools
    all_ps = sorted([''.join(i) for i in itertools.permutations(s)])
    if len(set(s)) != len(s):
        return 0
    else:
        return all_ps.index(s) + 1