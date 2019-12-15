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
        print(removePair(str(input())))
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
'''
Function Arguments :
		@param  : s(given string)
		@return : Modified String or "Empty String"
'''
def removePair(s):
    # code here
    import queue
    stack = queue.LifoQueue()
    r = ''
    stack.put(s[0])
    for i in range(1,len(s)):
        if stack.empty():
            stack.put(s[i])
        else:
            f = stack.get()
            if f != s[i]:
                stack.put(f)
                stack.put(s[i])
            else:
                stack.put(f)
                g = stack.get()
                if g == s[i]:
                    pass
    while (stack.empty() is not True):
        x = stack.get()
        r = x + r
    if r != '':
        return r
    else:
        return "Empty String"