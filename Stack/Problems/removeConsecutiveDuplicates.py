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
        print(removeConsecutiveDuplicates(str(input())))
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
'''
Function Arguments :
		@param  : s(given string)
		@return : Modified String
'''
def removeConsecutiveDuplicates(s):
    # code here
    tracker = []
    for i in s:
        if tracker != []:
            if tracker[-1] != i:
                tracker.append(i)
            else:
                continue
        else:
            tracker.append(i)
    return ''.join(tracker)