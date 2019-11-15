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
    
# Node class
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
#Linked list class
class LinkedList:
    def __init__(self):
        self.head=None
    # append at the end of the list
    def append(self,new_node):
        if self.head is None:
            self.head=new_node
            return
        curr_node=self.head
        while curr_node.next is not None:
            curr_node=curr_node.next
        curr_node.next=new_node
if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        n=int(input())
        a=LinkedList()
        nodes=list(map(int,input().strip().split())) #list containing nodes
        for x in nodes:
            node=Node(x) # create a new node
            a.append(node)
        print(getCount(a.head))
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
Your task is to return the count of elements
in the given linked list
Function Arguments: head_node (head of the linked list)
Return Type: Integer
	Contributed By: Nagendra Jha
'''
def getCount(head_node):
    #code here
    l = 0
    while head_node is not None:
        l += 1
        head_node = head_node.next
    return l