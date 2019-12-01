{
#Initial Template for Python 3
import atexit
import io
import sys
# Contributed by : Nagendra Jha
# Node Class
class Node:
    def __init__(self, data):  # data -> value stored in node
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
# prints the elements of linked list starting with head
def printList(head):
    if head is None:
        print(' ')
        return
    curr_node = head
    while curr_node:
        print(curr_node.data,end=" ")
        curr_node=curr_node.next
    print(' ')
if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        n = int(input())
        p = LinkedList() # create a new linked list 'a'.
        nodes_p = list(map(int, input().strip().split()))
        for x in nodes_p:
            p.append(x)  # add to the end of the list
        printList(mergeSort(p.head))

}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3

def sortedMerge(a,b):
    result = None
    if a == None:
        return b
    if b == None:
        return a
    if a.data <= b.data:
        result = a
        result.next = sortedMerge(a.next,b)
    else:
        result = b
        result.next = sortedMerge(a,b.next)
    return result
    
def getMiddle(head):
    if (head == None):
        return head

    slow = head
    fast = head

    while (fast.next != None and fast.next.next != None):
        slow = slow.next
        fast = fast.next.next
        
    return slow

def mergeSort(head):
    '''
    :param head: head of unsorted linked list 
    :return: head of sorted linkd list
    
    # Node Class
    class Node:
        def __init__(self, data):  # data -> value stored in node
            self.data = data
            self.next = None
    '''
    if head == None or head.next == None:
            return head
    middle = getMiddle(head)
    nexttomiddle = middle.next
    middle.next = None

    left = mergeSort(head)
    right = mergeSort(nexttomiddle)

    sortedlist = sortedMerge(left, right)
    return sortedlist