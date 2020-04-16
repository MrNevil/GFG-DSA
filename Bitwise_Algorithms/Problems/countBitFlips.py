"""
You are given two numbers A and B. Write a program to count number of bits 
needed to be flipped to convert A to B.

Input:
The first line of input contains an integer T denoting the number of test cases. 
T testcases follow. The first line of each test case is A and B separated by a 
space.

Output:
For each testcase, in a new line, print the number of bits needed to be flipped.

User Task:
The task is to complete the function countBitsFlip() that takes A and B as 
parameters and returns the count of the number of bits to be flipped to convert 
A to B.

Constraints:
1 ≤ T ≤ 100
1 ≤ A, B ≤ 10^3

Example:
Input:
2
10 20
20 25
Output:
4
3

Explanation:
Testcase 1:
A  = 01010
B  = 10100
As we can see, the bits of A that need to be flipped are 01010. If we flip these 
bits, we get 10100, which is equal to B.
Testcase 2:
A  = 10100
B  = 11001
As we can see, the bits of A that need to be flipped are 10100. If we flip these 
bits, we get 11001, which is equal to B.
"""
{
#Initial Template for Python 3
import math
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        ab=[int(x) for x in input().strip().split()]
        a=ab[0]
        b=ab[1]
        print(countBitsFlip(a,b))
        T-=1
if __name__=="__main__":
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
##Complete this function
def countBitsFlip(a,b):
    ##Your code here
    c = a ^ b
    cc = bin(c)[2:].count('1')
    return (cc)
