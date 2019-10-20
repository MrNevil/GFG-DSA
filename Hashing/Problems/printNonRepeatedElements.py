{
#Initial Template for Python 3
def main():
    T=int(input())
    while(T>0):
        
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        printNonRepeated(arr,n)
        print()
        
        T-=1
if __name__=="__main__":
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
#Complete this function
def printNonRepeated(arr,n):
    #Your code here
    import collections
    freqs = collections.Counter(arr)
    for i in arr:
        if freqs[i] == 1:
            print (i,end=" ")