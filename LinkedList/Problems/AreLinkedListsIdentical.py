{
# Node Class    
class node:
    def __init__(self, val):
        self.data = val
        self.next = None
        
# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None
    def insert(self, val):
        new_node = node(val)
        new_node.data = val
        new_node.next = self.head
        self.head = new_node
        
def printList(head):
    while head:
        print(head.data, end=' ')
        head=head.next
    print()
def createList(arr, n):
    lis = Linked_List()
    for i in range(n):
        lis.insert(arr[i])
    return lis.head
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        head1 = createList(arr, n)
        n = int(input())
        arr = list(map(int, input().strip().split()))
        head2 = createList(arr, n)
        if(areIdentical(head1, head2)):
            print('Identical')
        else:
            print('Not identical')
# Contributed by: Harshit Sidhwa
}
''' This is a function problem.You only need to complete the function given below '''
# your task is to complete this function
# function should return true/1 if both
# are identical else return false/0
'''
# Node Class    
class node:
    def __init__(self, val):
        self.data = val
        self.next = None
        
'''
def areIdentical(head1, head2):
    # Code here
    x1 = []
    curr_node = head1
    while curr_node != None:
        x1.append(curr_node.data)
        curr_node = curr_node.next
    x2 = []
    curr_node = head2
    while curr_node != None:
        x2.append(curr_node.data)
        curr_node = curr_node.next
    if x1 == x2:
        return True
    else:
        return False