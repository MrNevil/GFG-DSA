{
#Initial Template for Python 3
import math
    
def main():
        T=int(input())
        while(T>0):
            
            N=int(input())
            A=[int(x) for x in input().strip().split()]
            
            twoRepeated(A,N)
            print()
            
            T-=1
if __name__ == "__main__":
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
##Complete this code
def twoRepeated(arr,n):
    #Your code here
    twice_a = []
    for i in arr:
        if arr.count(i) == 2:
            if i not in twice_a:
                twice_a.append(i)
    a,b = twice_a[0],twice_a[1]
    ai,bi = arr.index(a),arr.index(b)
    if arr[ai+1:].index(a) < arr[ai+1:].index(b):
        print (' '.join([str(a),str(b)]),end = '')
    else:
        if a in arr[bi+1:] and b in arr[bi+1:]:
            ind_a = arr[bi+1:].index(a)
            ind_b = arr[bi+1:].index(b)
            if ind_a < ind_b:
                print (' '.join([str(a),str(b)]),end = '')
            else:
                print (' '.join([str(b),str(a)]),end = '')