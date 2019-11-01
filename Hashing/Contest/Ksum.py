"""
You are given an array of integers. Find the sum of first K smallest numbers. 

Input : 
First line of input contains number of testcases T. The 1st line of each testcase contains a two integers N denoting the number of elements in the array A and K. The 2nd line of each testcase, contains N space separated integers denoting the elements of the array A.

Output : 
For each testcase you need to print the sum of K smallest numbers.

Constraints :
1 <= T <= 50
1 <= N <= 105
1 <= K <= N
0 <= A[i] <= 106

Example :
Input :
1
6 4
1 3 4 1 3 8

Output :
8

Explaination :
Testcase1: Sum of first 4 smallest numbers is 1+1+3+3 = 8
"""

def ksum(arr,k):
    arr = sorted(arr)
    return sum(arr[:k])
    
if __name__ == '__main__':
    t = int(input())
    for tcase in range(t):
        N,K = list(map(int,input().strip().split()))
        arr = list(map(int,input().strip().split()))
        print (ksum(arr,K))