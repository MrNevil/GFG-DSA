"""
Find the minimum number of Operations required to make N to 1:
    Following Operations are allowed:
        1. If N is even then divide N by 2
        2 if N is odd, then add or subtract 1 from N.
"""

def minOperations(N):
    if N == 1:
        return 0
    elif N%2 == 0:
        return (1 + minOperations(N/2))
    else:
        return (1 + min(minOperations(N-1),minOperations(N+1)))
    
if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        N = int(input())
        print (minOperations(N))