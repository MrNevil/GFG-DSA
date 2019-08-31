{
#Initial Template for Python 3
//Position this line where user code will be pasted.
def main():
    testcases=int(input())
    
    while(testcases>0):
        sizeOfArray=int(input())
        
        arr=[int(x) for x in input().strip().split()]
        
        element=int(input())
        
        insertAtEnd(arr,sizeOfArray,element)
        
        for i in arr:
            print(i,end=" ")
        print()
        
        testcases-=1
    
if __name__=="__main__":
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
# You only need to insert the given element at 
# the end, i.e., at index sizeOfArray - 1. You may 
# assume that the array already has sizeOfArray - 1
# elements. 
def insertAtEnd(arr,sizeOfArray,element):
    ##Your code here
    arr.append(element)