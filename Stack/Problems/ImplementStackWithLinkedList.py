{

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = Stack()
        q = int(input())
        q1 = list(map(int, input().split()))
        i = 0
        while(i < len(q1)):
            if(q1[i] == 1):
                s.push(q1[i + 1])
                i = i + 2
            elif(q1[i] == 2):
                print(s.pop(), end=" ")
                i = i + 1
            elif(s.isEmpty()):
                print(-1)
        print()

}
''' This is a function problem.You only need to complete the function given below '''
# Class to represent a node
class StackNode:
    def __init__(self,data):
        self.data = data
        self.next = None
		
class Stack:
    # The method push to push element into
    # the stack
    def __init__(self):
        self.head = None
    def push(self, data):
        # Add code here
        # The method pop which return the element
        # poped out of the stack
        new_node = StackNode(data)
        if self.head is None:
            self.head = new_node
            return
        new_node = StackNode(data)
        new_node.next = self.head
        self.head = new_node
    def pop(self):
        # Add code here
        if self.head is None:
            return -1
        popped_data = self.head.data
        self.head = self.head.next
        return popped_data
    def isEmpty(self):
        if self.head:
            return False
        return True