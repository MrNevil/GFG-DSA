"""
You are given a decimal number N. You need to find the gray code of the number 
n and conver it into decimal.
To see how it's done, refer here.

Input Format:
The first line contains an integer T, the number of test cases. For each test 
case, there is an integer N denoting the number

Output Format:
For each test case, the output is gray code equivalent of N.

User Task:
The task is to complete the function greyConverter() which takes n parameter 
and returns gray code.

Constraints:
1 <= T <= 100
0 <= N <= 108

Example:
Input:
3
7
10
0

Output:
4
15
0

Explanation:
Testcase1: 7 is represented as 111 in binary form. The gray code of 111 is 100, 
in the binary form whose decimal equivalent is 4.
Testcase2: 10 is represented as 1010 in binary form. The gray code of 1010 is 
1111, in the binary form whose decimal equivalent is 15.
Testcase3: Zero is represented as zero in binary, gray, and decimal.
"""
{
#Initial Template for Python 3
import math
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        print(greyConverter(n))
        T-=1
if __name__=="__main__":
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
##Complete this fcuntion
def greyConverter(n):
    ##Your code here
    bin_rep = bin(n)[2:]
    gray = bin_rep[0]
    for i in range(1,len(bin_rep)):
        gray += str(int(bin_rep[i-1]) ^ int(bin_rep[i]))
    return int(gray,2)