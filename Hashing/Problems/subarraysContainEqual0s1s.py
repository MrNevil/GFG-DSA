{
#Initial Template for Python 3
def main():
    T=int(input())
    while(T>0):
        
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        
        
        print(countSubarrWithEqualZeroAndOne(arr, n))
        
        T-=1
if __name__=="__main__":
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
#Complete this function

def allSubArrays(L,L2=None):
    if L2==None:
        L2 = L[:-1]
    if L==[]:
        if L2==[]:
            return []
        return allSubArrays(L2,L2[:-1])
    return [L]+allSubArrays(L[1:],L2)
    
def countSubarrWithEqualZeroAndOne(arr, n):
    #Your code here
    C = 0
    allsubarrays = allSubArrays(arr)
    for a in allsubarrays:
        if a.count(0) == a.count(1):
            C += 1
    return C