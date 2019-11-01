"""
Given an array of positive element having size N and an integer C. Check if there exists a pair (A,B) such that A xor B = C.

Input : 
First line of input contains number of testcases T. The 1st line of each testcase contains a two integers N and C. The 2nd line of each testcase, contains N space separated integers denoting the elements of the array A.

Output: 
Print "Yes" is the pair exists else print "No" without quotes.(Change line after every answer).

Constraints:
1 <= T <= 100
1 <= N <= 105
1 <= C <= 105
0 <= arr[i] <= 105

Example:
Input:
2
7 7
2 1 10 3 4 9 5 
5 1
9 9 10 10 3 

Output:
Yes
No

Explanation :
In first case, pair (2,5) give 7. Hence answer is "Yes". In second case no pair exist such that satisfies the condition hance the answer is "No".
"""

def XORPair(arr,n,c):
    result = 0
    s = set()
    for i in range(n):
        if (c ^ arr[i]) in s:
            result += 1
        s.add(arr[i])
    if result > 0:
        return "Yes"
    else:
        return "No"
        
if __name__ == '__main__':
    t = int(input())
    for tcase in range(t):
        N,C = list(map(int,input().strip().split()))
        arr = list(map(int,input().strip().split()))
        print (XORPair(arr,N,C))