"""
Given two integers ‘a’ and ‘m’. The task is to find modular multiplicative 
inverse of ‘a’ under modulo ‘m’.
Note: Print the smallest modular multiplicative inverse.

Input:
First line consists of T test cases. Only line of every test case consists of 2 
integers 'a' and 'm'.

Output:
For each testcase, in a new line, print the modular multiplicative inverse if 
exists else print -1.

Your Task:
This is a function problem. You just need to complete the function modInverse() 
that takes a and m as parameters and returns modular multiplicative inverse of 
‘a’ under modulo ‘m’.

Constraints:
1 <= T <= 100
1 <= m <= 100

Example:
Input:
2
3 11
10 17
Output:
4
12

Explanation:
Testcase 1:
Input:  a = 3, m = 11
Output: 4
Since (4*3) mod 11 = 1, 4 is modulo inverse of 3
One might think, 15 also as a valid output as "(15*3) mod 11" 
is also 1, but 15 is not in ring {0, 1, 2, ... 10}, so not valid.
Testcase 2:
Input:  a = 10, m = 17
Output: 12
Since (12*10) mod 17 = 1, 12 is the modulo inverse of 10.
 
"""
{
#Initial Template for Python 3
import math
//Position this line where user code will be pasted.
    
    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        am=[int(x) for x in input().strip().split()]
        a=am[0]
        m=am[1]
        print(modInverse(a,m))
        
        
        T-=1
    
    
if __name__=="__main__":
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
##Complete this function
def modInverse(a,m):
    ##Your code here
    a = a%m
    for x in range(1,m):
        if ((a*x)%m) == 1:
            return x
    return -1
