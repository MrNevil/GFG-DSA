{
#Initial Template for Python 3
def main():
    T=int(input())
    while(T>0):
        sizeOfArr=int(input())
        arr=[int(x) for x in input().strip().split()]
        
        arrayReversal(arr,sizeOfArr)
        for i in arr:
            print(i,end=" ")
            
        print()
        
        T-=1
if __name__=="__main__":
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
#Complete this function
def arrayReversal(arr,sizeOfArr):
    #Your code here
    temp = 0
    low,high = 0,sizeOfArr-1
    while low < high:
        temp = arr[low]
        arr[low]= arr[high]
        arr[high] = temp
        low += 1
        high -= 1