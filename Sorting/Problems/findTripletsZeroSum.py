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
        n=int(input())
        a=list(map(int,input().strip().split()))
        print(findTriplets(a,n))
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
''' Your task is to returns 1 if there is triplet with sum equal
    to 0 present in A[], else return 0'''
    
def isPair(arr,left,right,u):
    while left < right:
        if arr[left] + arr[right] < u:
            left += 1
        elif arr[left] + arr[right] == u:
            return True
        elif arr[left] + arr[right] > u:
            right -= 1
    return False

def findTriplets(a,n):
    #code here
    a = sorted(a)
    for i in range(n):
        if isPair(a,i+1,n-1,0-a[i]):
            return 1
    return 0