{
#Initial Template for Python 3
//Position this line where user code will be pasted.
    
# Driver Code
def main():
    
    # testcase input
    testcases = int(input())
    
    # looping through all testcases
    while testcases > 0:
        
        sizeOfArray = int(input())
        
        arr = [int(x) for x in input().split()]
        
        maximumAdjacent(sizeOfArray, arr)
        
        print()
        
        testcases -= 1
if __name__ == '__main__':
    main()
    
    
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
# Function to find maximum of all adjacents
def maximumAdjacent(sizeOfArray, arr):
    
    # Your code here
    # Function should print max of all adjacents
    for i in range(len(arr)-1):
        print (max(arr[i],arr[i+1]),end=" ")