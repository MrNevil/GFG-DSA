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
        n,sum=map(int,input().strip().split())
        a=list(map(int,input().strip().split()))
        print(find3Numbers(a,n,sum))
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
''' Your task is to returns 1 if there is triplet with sum equal
    to 'sum' present in A[], else return 0'''
    
def find3Numbers(a,n,s):
    #code here
    a = sorted(a)
    for i in range(n):
        if isPair(a,i+1,n-1,s-a[i]):
            return 1
    return 0

def isPair(a,left,right,u):
    while left < right:
        if a[left]+a[right] == u:
            return True
        elif a[left] + a[right] < u:
            left += 1
        elif a[left] + a[right] > u:
            right -= 1
    return False