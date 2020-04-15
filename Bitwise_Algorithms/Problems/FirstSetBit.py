"""
Given an integer an N. The task is to print the position of first set bit found from 
right side in the binary representation of the number.

Input:
The first line of the input contains an integer T, denoting the number of test 
cases. Then T test cases follow. The only line of the each test case contains 
an integer N.

Output:
For each test case print in a single line an integer denoting the position of 
the first set bit found form right side of the binary representation of the 
number. If there is no set bit print "0".

User Task:
The task is to complete the function getFirstSetBit() that takes n as parameter 
and returns the the position of first set bit.

Constraints:
1 <= T <= 200
0 <= N <= 106

Example:
Input:
3
18
12
0

Output:
2
3
0

Explanation:
Testcase 1: Binary representation of 18 is 010010, the first set bit from the 
right side is at position 2.
Testcase 2: Binary representation of  12 is 1100, the first set bit from the 
right side is at position 3.
Testcase 3: In 0 there is no set bit so we print 0 as mentioned.
"""
{
#Initial Template for Python 3
import math
//Position this line where user code will be pasted.
    
    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        
        print(getFirstSetBit(n))
        
        
        T-=1
    
    
if __name__=="__main__":
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
##Complete this function
def getFirstSetBit(n):
    #Your code here
    bin_rep = bin(n)
    req_bin_rep = bin_rep[1:][::-1]
    if '1' not in req_bin_rep:
        return "0"
    else:
        for ind,val in enumerate(req_bin_rep):
            if val == '1':
                break
        return (ind+1)