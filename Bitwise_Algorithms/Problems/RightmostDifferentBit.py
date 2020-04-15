"""
Given two numbers M and N. The task is to find the position of rightmost 
different bit in binary representation of numbers.

Input Format:
The input line contains T, denoting the number of testcases. Each testcase 
follows. First line of each testcase contains two space separated integers M and 
N.

Output Format:
For each testcase in new line, print the position of rightmost different bit in 
binary representation of numbers. If both M and N are same then print -1 in this 
case.

User Task:
The task is to complete the function posOfRightMostDiffBit() which takes two 
arguments m and n and returns the position of first different bits in m and n.

Constraints:
1 <= T <= 100
1 <= M <= 10^3
1 <= N <= 10^3

Example:
Input:
2
11 9
52 4

Output:
2
5

Explanation:
Tescase 1: Binary representaion of the given numbers are: 1011 and 1001, 2nd bit 
from right is different.
Testcase 2: Binary representation of the given numbers are:  ‭110100‬ and 0100, 
5th bit fron right is different.

"""
{
#Initial Template for Python 3
import math
def getRightMostSetBit(n):
    return math.log2(n&-n)+1
    //Position this line where user code will be pasted.
    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        mn=[int(x) for x in input().strip().split()]
        m=mn[0]
        n=mn[1]
        
        print(math.floor(posOfRightMostDiffBit(m,n)))
        
        
        
        
        T-=1
    
    
if __name__=="__main__":
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
##Complete this function
def posOfRightMostDiffBit(m,n):
    #Your code here
    if m==n:
        return -1
    else:
        num = ~(m^n)
        k = 1
        while True:
            if (num & (1<<(k-1)))==0:
                return k
            else:
                k += 1