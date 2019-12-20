{
#Initial Template for Python 3
import atexit
import io
import sys
#Contributed by :Nagendra Jha
_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER
@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        k = 0
        m = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(a[k])
                k+=1
            m.append(row)
        print(getId(m,n))
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
'''
Function Arguments :
		@param  :m (boolean matrix of size n*n), n(no of rows and cols )
		@return : Integer
'''
def getId(m,n):
    # code here
    v = []
    for j in range(n):
        cnt = 0
        for i in range(n):
            if m[i][j] == 1:
                cnt += 1
        if cnt >= n-1:
            v.append(j)
    if len(v) == 1:
        return v[0]
    else:
        return -1