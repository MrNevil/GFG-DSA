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
        a = list(map(str,input().strip().split()))
        stack = [] # our stack to be implemented
        i = 0 #current index
        while i < len(a):
            if a[i]=='i':
                insert(stack,a[i+1])
                i+=1
            elif a[i] == 'f' :
                if(find(stack,a[i+1])):
                    print("Yes")
                else:
                    print("No")
                i+=1
            elif a[i] == 'r' :
                (remove(stack))
            else:
                print(headOf_Stack(stack))
            i+=1
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
'''
Function Arguments :
		@param  : stack (given list on which stack is implemented)
		@param  : x (value to be used accordingly)
		@return : None
'''
def insert(stack,x):
    # code here
    stack.append(x)
def find(stack,x):
    #code here
    for i in stack:
        if i == x:
            return True
    return False
def headOf_Stack(stack):
    #code here
    if stack:
        return stack[len(stack)-1]
def remove(stack):
    #code here
    if stack:
        stack.pop(len(stack)-1)