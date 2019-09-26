"""
You are given a matrix Mat of m rows and n columns. The matrix is boolean so the elements of the matrix can only be either 0 or 1.
Now, if any row of the matrix contains a 1, then you need to fill that whole row with 1. After doing the mentioned operation, you need to print the modified matrix.

Input:
The first line of input contains T denoting the number of testcases. T testcases follow.
The first line of each testcase contains m and n denoting number of rows and number of columns.
Then next m lines contain n elements denoting the elements of the matrix.

Output:
For each testcase, in a new line, print the modified matrix.

Constraints:
1 <= T <= 100
1 <= m, n <= 900
Matij ∈ {0,1}

Examples:
Input:
2
5 4
1 0 0 0
0 0 0 0
0 1 0 0
0 0 0 0
0 0 0 1
1 2
0 0
Output:
1 1 1 1
0 0 0 0
1 1 1 1
0 0 0 0
1 1 1 1
0 0

Explanation:
Testcase1: rows = 5 and columns = 4
The given matrix is
1 0 0 0
0 0 0 0
0 1 0 0
0 0 0 0
0 0 0 1
Evidently, the first row contains a 1 so fill the whole row with 1. The third row also contains a 1 so that row will be filled too. Finally, the last row contains a 1 and therefore it needs to be filled with 1 too.
The final matrix is
1 1 1 1
0 0 0 0
1 1 1 1
0 0 0 0
1 1 1 1

"""

def modified_matrix(arr,m,n):
    for i in range(m):
        if '1' in arr[i]:
            arr[i] = ['1'] * n
    x = [" ".join(h) for h in arr]
    return "\n".join(x)
    
if __name__ == '__main__':
    T = int(input())
    for tcase in range(T):
        M,N = list(map(int,input().strip().split()))
        arr = []
        for r in range(M):
            row = list(map(str,input().strip().split()))
            arr.append(row)
        print (modified_matrix(arr,M,N))