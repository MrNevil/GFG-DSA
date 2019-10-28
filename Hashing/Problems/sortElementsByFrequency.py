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
        a = list(map(int, input().strip().split()))
        sortByFreq(a,n)
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
'''
	Your task is to sort the elements according
	to the frequency of their occurence
	in the given array.
	
	Function Arguments: array a with size n. 
	Return Type:none, print the sorted array
'''
def sortByFreq(a,n):
    #code here
    import collections
    import operator
    freqs = collections.Counter(a)
    out = sorted(freqs.items(),key=operator.itemgetter(1),reverse=True)
    gr1,eq1 = [],[]
    for x,y in out:
        if y > 1:
            gr1.append(x)
        elif y == 1:
            eq1.append(x)
    output = []
    for y in gr1:
        output.extend([y]*a.count(y))
    output += sorted(eq1)
    print (" ".join(str(u) for u in output))