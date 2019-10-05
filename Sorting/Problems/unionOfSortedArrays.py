{
#Initial Template for Python 3
import atexit
import io
import sys
#Contributed by : Nagendra Jha
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,m = map(int,input().strip().split())
        a = list(map(int,input().strip().split()))
        b = list(map(int,input().strip().split()))
        mergeArrays(a,b,n,m)
        print()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
def mergeArrays(a,b,n,m):
    '''
    :param a: given sorted array a
    :param n: size of sorted array a
    :param b: given sorted array b
    :param m: size of sorted array b
    :return: None, print the union, space separated
    '''
    # code here 
    a = set(a)
    b = set(b)
    print (' '.join(str(i) for i in sorted(a.union(b))),end="")