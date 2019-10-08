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
        n,m,p = map(int, input().strip().split())
        A = list(map(int, input().strip().split()))
        B = list(map(int, input().strip().split()))
        C = list(map(int, input().strip().split()))
        print(*(mergeThree(A,B,C)))
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
def mergeThree(A,B,C):
    #code here
    return sorted(A+B+C)