{
#Initial Template for Python 3
import atexit
import io
import sys
# This code is contributed by Nikhil Kumar Singh(nickzuck_007)
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
        exp = str(input())
        print('{0:g}'.format(float(EvaluatePostfix(exp))))
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
'''
Function Arguments :
		@param  : exp (given postfix expression)
		@return : return the desired value
'''
def EvaluatePostfix(exp):
    #code here
    stack = []
    for char in exp:
        if char in ['*','/','+','-']:
            a = stack.pop()
            b = stack.pop()
            res = eval(str(b) + char + str(a))
            stack.append(res)
        else:
            stack.append(char)
    return stack[-1]