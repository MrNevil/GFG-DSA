{
#Initial Template for Python 3
import io
import sys
#Contributed by : Nagendra Jha
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,m = map(int,input().strip().split())
        a = list(map(int,input().strip().split()))
        b = list(map(int,input().strip().split()))
        printIntersection(a,b,n,m)
        print()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
def printIntersection(a, b, n, m):
    '''
    :param a: given sorted array a
    :param n: size of sorted array a
    :param b: given sorted array b
    :param m: size of sorted array b
    :return: print intersection list of these two arrays or -1
    '''
    # code here
    inter = sorted(set(a).intersection(set(b)))
    if inter:
        print (" ".join(str(i) for i in inter),end="")
    else:
        print (-1,end="")