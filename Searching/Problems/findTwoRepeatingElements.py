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
    import collections
    twice_a = collections.defaultdict(list)
    for i in arr:
        if arr.count(i) == 2:
            temp = [k for k,v in enumerate(arr) if v == i]
            twice_a[i] = temp
    keys = list(twice_a.keys())
    if twice_a[keys[0]][1] < twice_a[keys[1]][1]:
        print (' '.join([str(keys[0]),str(keys[1])]),end = '')
    else:
        print (' '.join([str(keys[1]),str(keys[0])]),end = '')