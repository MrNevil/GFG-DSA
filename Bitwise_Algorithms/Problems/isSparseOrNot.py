"""
Given a number N.  The task is to check whether it is sparse or not. A number is 
said to be a sparse number if no two or more consecutive bits are set  in the 
binary representation.

Input:
The first line of input contains an integer T denoting the number of test cases. 
The first line of each test case is number 'N'.

Output:
Print '1' if the number is sparse and '0' if the number is not sparse.

User Task:
The task is to complete the function checkSparse() that takes n as parameter 
and returns true if the number is sparse else returns false.

Constraints:
1 <= T <= 100
1 <= N <= 103

Example:
Input:
2
2
3

Output:
1
0

Explanation:
Testcase 1: Binary Representation of 2 is 10, which is not having consecutive 
set bits. So, it is sparse number.
Testcase 2: Binary Representation of 3 is 11, which is having consecutive set 
bits in it. So, it is not a sparse number.
"""

{
#Initial Template for Python 3
import math
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        if isSparse(n):
            print("1")
        else:
            print("0")
        T-=1
if __name__=="__main__":
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
##Complete this function
def isSparse(n):
    #Your code here
    bin_rep = bin(n)[2:]
    k = bin_rep[0]
    for i in range(len(bin_rep[1:])):
        if k == '1':
            if bin_rep[1:][i] == k:
                return False
            else:
                k = bin_rep[1:][i]
        else:
            k = bin_rep[1:][i]
    return True