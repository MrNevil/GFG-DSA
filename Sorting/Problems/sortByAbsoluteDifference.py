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
    for tt in range(t):
        n,k = map(int, input().strip().split())
        a = list(map(int, input().strip().split()))
        print(*sortAbs(a,n,k))
        
    	 
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
'''
	Your task is to stable sort the array according to
	increasing order of absolute differences with the
	given constant k.
	
	Function Arguments: array (a), size of array (n), constant value(k)
	Return Type: none, you just have to modify the array
'''
def sortAbs(a, n, k):
    #code here
    tmp = 0
    from collections import defaultdict,OrderedDict
    import operator
    diff_dict = OrderedDict()
    for i in range(n):
        if a[i] in diff_dict:
            diff_dict[a[i]].append(abs(a[i]-k))
        else:
            diff_dict[a[i]] = []
            diff_dict[a[i]].append(abs(a[i]-k))
    result = sorted(diff_dict.items(),key=operator.itemgetter(1))
    res = []
    [res.extend([a]*len(b)) for a,b in result]
    return res