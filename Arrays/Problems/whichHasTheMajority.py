{

if __name__ == '__main__':
    T=int(input())
    while(T>0):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        
        x,y=map(int,input().strip().split())
        
        print(majorityWins(arr,n,x,y))
        T-=1

}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
#Complete this function
def majorityWins(arr, n,  x,y):
    import collections
    # code here
    counts = collections.Counter(arr)
    if counts[x] > counts[y]:
        return x
    elif counts[x] < counts[y]:
        return y
    else:
        return min(x,y)
