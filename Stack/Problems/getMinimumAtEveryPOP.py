{
#Initial Template for Python 3
import atexit
import io
import sys
#Contributed by : Nagendra Jha
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
        stack =  _push(a,n) # our stack to be used
        _getMinAtPop(stack) # print elements of stack as required
        print()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
def _push(a,n):
    '''
    :param a: given array
    :param n: given size of array
    :return: stack
    '''
    # code here
    stack = []
    min_el = a[0]
    for i in range(0,n):
        if min_el > a[i]:
            min_el = a[i]
        stack.append(min_el)
    return stack
    
def _getMinAtPop(stack):
    '''
    :param stack: our stack
    :return: none, print the elements in order of pop one by one, new line is not required
    '''
    # code here
    n = len(stack)
    while n > 0:
        print (stack.pop(),end = " ")
        n -= 1