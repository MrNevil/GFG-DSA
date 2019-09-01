{
# Initial Template for Python 3
import math
def main():
    T = int(input())
    while(T > 0):
        N = int(input())
        A = [int(x) for x in input().strip().split()]
        print(equilibriumPoint(A, N))
        T -= 1
if __name__ == "__main__":
    main()

}
''' This is a function problem.You only need to complete the function given below '''
# User function Template for python3
# Complete this function
def equilibriumPoint(A, N):
    # Your code here
    total = sum(A)
    r = 0
    for index in range(N-1, -1, -1):
        l = total - r - A[index]
        if l==r:
            return index+1
        r += A[index]
    return -1