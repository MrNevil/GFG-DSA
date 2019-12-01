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
    
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            return
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = new_node
if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        n,nth_node = map(int, input().strip().split())
        a = LinkedList() # create a new linked list 'a'.
        nodes_a = list(map(int, input().strip().split()))
        for x in nodes_a:
            a.append(x)  # add to the end of the list
        print(getNthfromEnd(a.head,nth_node))
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
'''
	Your task is to return the data stored in
	the nth end from end of linked list.
	
	Function Arguments: head (reference to head of the list), n (pos of node from end)
	Return Type: Integer or -1 if no such node exits.
	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
'''
def getNthfromEnd(head,n):
    #code here
    l_list = 0
    curr_node = head
    while curr_node != None:
        l_list += 1
        curr_node = curr_node.next
    if n > l_list:
        return -1
    curr_node = head
    C = 0
    while curr_node != None:
        if C == l_list - n:
            return curr_node.data
        C += 1
        curr_node = curr_node.next