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
        
        largestAndSecondLargest(sizeOfArray, arr)
        
        testcases -= 1
if __name__ == '__main__':
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
# Function to find largest and second largest element in the array
def largestAndSecondLargest(sizeOfArray, arr):
    max1 = -1
    max2 = -1
    
    ''''''''''''''''''''''''''''''''''''''''''''''''
    ''' Your code here'''
    ''' Function should print max and second max '''
    ''''''''''''''''''''''''''''''''''''''''''''''''
    max1 = max(arr)
    others = []
    for i in arr:
        if i!=max1:
            others.append(i)
    if others:
        max2 = max(others)
    else:
        max2 = -1
    print (max1, max2)