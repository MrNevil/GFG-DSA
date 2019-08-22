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
        s = str(input())
        ans = powerSet(s)
        ans.sort()
        print(*ans)
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
def powerSet(s):
    '''
    :param s: given string s
    :return: list containing power set of s.
    '''
    perm = []
    if len(s) == 0:
        perm.append("")
        return perm
    first = s[0]
    rem = s[1:len(s)]
    words = powerSet(rem)
    perm.extend(words)
    for word in words:
        perm.append(first+word)
    return perm