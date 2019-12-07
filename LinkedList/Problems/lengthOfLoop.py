{

class Node:
    data=0
    next=None
    
    
def newNode(data):
    temp=Node()
    temp.data=data
    temp.next=None
    return temp
    
def insert(head,data):
    if(head==None):
        head=newNode(data)
    else:
        head.next=insert(head.next,data)
    return head
def makeLoop(head,x):
    curr=head
    last=head
    counter=0
    while(counter<x):
        
        curr=curr.next
        counter+=1
    while(last.next!=None):
        last=last.next
    last.next=curr
            
def main():
    testcases=int(input())
    
    while(testcases>0):
        head=Node()
        head=None
        sizeOfArray=int(input())
        arr=[int(x) for x in input().strip().split()]
        x=int(input())
        
        for i in arr:
            head=insert(head,i)
        
        if x!=0:
            makeLoop(head,x)
        
        print(countNodesinLoop(head))
        
        testcases-=1
if __name__=="__main__":
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
'''
Structure of node
class Node:
    data=0
    next=None
    
    
def newNode(data):
    temp=Node()
    temp.data=data
    temp.next=None
    return temp
'''

def count(ptr):
    c = 1
    temp = ptr
    while temp.next != ptr:
        c += 1
        temp = temp.next
    return c
    
def countNodesinLoop(head):
    #Your code here
    if head == None and head.next==None:
        return 0
    current = head
    fast = current.next.next
    slow = current.next
    while (fast!=None and fast.next!=None):
        if fast==slow:
            return count(slow)
        fast = fast.next.next
        slow = slow.next
    return 0