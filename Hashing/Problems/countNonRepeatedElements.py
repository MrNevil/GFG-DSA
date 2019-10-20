{
#Initial Template for Python 3
def main():
    T=int(input())
    while(T>0):
        
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        print(countNonRepeated(arr,n))
        
        
        T-=1
if __name__=="__main__":
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
##Complete this code
def countNonRepeated(arr,n):
    #Your code here
    import collections
    freqs = collections.Counter(arr)
    C = 0
    for k,v in freqs.items():
        if v == 1:
            C += 1
    return C