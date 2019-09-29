{

if __name__=="__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
    
        insert(arr)
    
        for i in range(n):
            print(arr[i],end=" ")
    
        print()
}
''' This is a function problem.You only need to complete the function given below '''
#Sort the array using insertion sort
def insert(arr):
    #add code here
    n = len(arr)
    for v in range(n):
        temp = arr[v]
        u = v
        while ((u > 0) & (temp < arr[u-1])):
            arr[u] = arr[u-1]
            u-=1
        arr[u] = temp