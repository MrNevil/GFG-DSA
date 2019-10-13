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
    
if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        n,m = map(int, input().strip().split())
        values = list(map(int, input().strip().split()))
        k = 0
        a=[]
        for i in range(n):
            row=[]
            for j in range(m):
                row.append(values[k])
                k+=1
            a.append(row)
        BoundaryTraversal(a,n,m)

}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
''' 
    Your task is to print boundary traversal
	of a given matrix.
	
	Function Arguments : a(given array), n (no of rows), m (no of columns). 
	Return Type: none, you have to print the result.
'''
def BoundaryTraversal(a,n,m):
    #code here
    firstRow = a[0]
    lastCol = []
    lastRow = []
    firstCol = []
    if n > 1 and m >= 1:
        r,c = 1,m-1
        while r < n:
            lastCol.append(a[r][c])
            r += 1
        lastRow = a[n-1][:(m-1)][::-1]
        firstCol = []
        if m > 1:
            r,c = 1,0
            while r < n-1:
                firstCol.append(a[r][c])
                r += 1
    boundary = firstRow + lastCol + lastRow + firstCol[::-1]
    print (" ".join(str(h) for h in boundary))