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
queue_1 = [] # first queue
queue_2 = [] # second queue
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        i = 0
        while i<len(a):
            if a[i] == 1:
                push_in_stack(a[i+1])
                i+=1
            else:
                print(pop_from_stack(),end=" ")
            i+=1
        # clear both the queues
        queue_1 = []
        queue_2 = []
        print()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
'''
    :param x: value to be inserted
    :return: None
    queue_1 = [] # first queue
    queue_2 = [] # second queue
    '''
def push_in_stack(x):
    
    # global declaration
    global queue_1
    global queue_2
    # code here
    queue_1.append(x)
    
def pop_from_stack():
    '''
    :return: the value of top of stack and pop from it.
    '''
    
    # global declaration
    global queue_1
    global queue_2
    # code here
    if queue_1:
        popped = queue_1.pop(len(queue_1)-1)
        return popped
    else:
        return -1