{
#Initial Template for Python 3
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None
class DoublyLinkedList:
	def __init__(self):
		self.head = None
	def append(self, new_data):
		new_node = Node(new_data)
		new_node.next = None
		if self.head is None:
			new_node.prev = None
			self.head = new_node
			return
		last = self.head
		while(last.next is not None):
			last = last.next
		last.next = new_node
		new_node.prev = last
		return
	def printList(self, node):
		while(node.next is not None):
			node = node.next
		while node.prev is not None:
		    node = node.prev
		while(node is not None):
		    print(node.data, end=" ")
		    node = node.next
		print()
		
		
		
		
        
def printList(node): 
        temp = node 
      
        while(node is not None): 
            print (node.data,end=" ")
            temp = node 
            node = node.next
        print()
        while(temp): 
            print (temp.data,end=" ") 
            temp = temp.prev 
		
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        llist = DoublyLinkedList()
        for e in arr:
            llist.append(e)
        llist.head=sortDoubly(llist.head)
        printList(llist.head)
        print()
def addNode(head, p, data):
    # Code here
    temp = head
    while p!=0:
        temp=temp.next
        p-=1
    n = Node(data)
    if temp.next is not None:
        n.next = temp.next
        temp.next.prev = n
        n.prev = temp
        temp.next = n
    else:
        n.prev = temp
        temp.next=  n
        

}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
'''
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None
'''

def sortedMerge(a,b):
    result = None
    if a == None:
        return b
    if b == None:
        return a
    if a.data <= b.data:
        result = a
        result.next = sortedMerge(a.next,b)
        result.next.prev = a
        result.prev = None
    else:
        result = b
        result.next = sortedMerge(a,b.next)
        result.next.prev = b
        result.prev = None
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

def sortDoubly(head):
    #Your code here
    if head == None or head.next == None:
            return head
    middle = getMiddle(head)
    nexttomiddle = middle.next
    middle.next = None

    left = sortDoubly(head)
    right = sortDoubly(nexttomiddle)

    sortedlist = sortedMerge(left, right)
    return sortedlist