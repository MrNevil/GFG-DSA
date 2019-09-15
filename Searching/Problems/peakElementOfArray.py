{
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        index = peakElement(arr, n)
        flag = False
        if index == 0 and n==1:
            flag = True
        elif index==0 and arr[index]>arr[index+1]:
            flag = True
        elif index==n-1 and arr[index]>arr[index-1]:
            flag = True
        elif arr[index-1] < arr[index] and arr[index] > arr[index+1]:
            flag = True
        else:
            flag = False
        if flag:
            print(1)
        else:
            print(0)
# Contributed by: Harshit Sidhwa

}
''' This is a function problem.You only need to complete the function given below '''
# your task is to complete this function
# function should return index to the any valid peak element
def peakElement(arr, n):
    # Code here
    return arr.index(max(arr))