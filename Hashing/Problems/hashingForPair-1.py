{
#Initial Template for Python 3
//Position this line where user code will be pasted.
def main():
    testcases=int(input())
    while(testcases>0):
        
        sizeOfArray=int(input())
        
        arr=[int(x) for x in input().strip().split()]
        
        sum=int(input())
        
        
        print(sumExists(arr,sizeOfArray,sum))
        
        testcases-=1
        
        
if __name__=="__main__":
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
##Complete this function
def sumExists(arr,sizeOfArray,sum):
    ##Your code here
    arr = sorted(arr)
    left,right = 0,sizeOfArray-1
    while left < right:
        if arr[left] + arr[right] < sum:
            left += 1
        elif arr[left] + arr[right] == sum:
            return 1
        elif arr[left] + arr[right] > sum:
            right -= 1
    return 0