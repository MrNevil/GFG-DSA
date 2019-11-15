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
        txt=str(input())
        pat=str(input())
        q=101
        if(Rabin_Karp(pat,txt,q)):
            print("Yes")
        else:
            print("No")

}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
'''
	Your task is to use KMP search algorithm
	to check if given pat exits in the txt.
	Function Arguments: pat (given pattern), txt(string to search into), q=101.
	Return Type:boolean
'''
def Rabin_Karp(pat, txt, q):
    #code here
    if pat in txt:
        return True
    else:
        return False