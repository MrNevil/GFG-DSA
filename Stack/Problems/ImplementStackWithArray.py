{
#Initial Template for Python 3
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        s=MyStack()
        q=int(input())
        q1=list(map(int,input().split()))
        i=0
        while(i<len(q1)):
            if(q1[i]==1):
                s.push(q1[i+1])
                i=i+2
            elif(q1[i]==2):
                print(s.pop(),end=" ")
                i=i+1
            elif(s.isEmpty()):
                print(-1)
                i=i+1
        print()   
}
''' This is a function problem.You only need to complete the function given below '''
# You need to write code for push() and pop()
class MyStack:
    
    def __init__(self):
        self.arr=[]
    
    #Adds element to the Stack
    def push(self,data):
        #add code here
        self.arr.append(data)
    
    #Removes element from the stack
    def pop(self):
        #add code here
        if self.arr:
            popped = self.arr.pop()
            return popped
        else:
            return -1