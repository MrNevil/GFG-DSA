# Python3 program for finding  
# number of divisor 
  
# program for finding  
# no. of divisors 
"""
Given a positive integer value N. The task is to find how many numbers less than 
or equal to N have numbers of divisors exactly equal to 3.

Input:
The first line contains integer T, denoting number of test cases. Then T test 
cases follow. The only line of each test case contains an integer N.

Output:
For each testcase, in a new line, print the answer of each test case.

Your Task:
This is a function problem. You only need to complete the function 
exactly3Divisors() that takes N as parameter and returns count of numbers less 
than or equal to N with exactly 3 divisors.

Constraints :
1 <= T <= 10^5
1 <= N <= 10^9

Example:
Input :
3
6
10
30
Output :
1
2
3

Explanation:
Testcase 1: There is only one number 4 which has exactly three divisors 1, 2 and 
4.
Testcase 2: 4 and 9 are the only two numbers less than or equal to 10 that have 
exactly three divisors.
Testcase 3: 4, 9, 25 are the only numbers less than or equal to 30 that have 
exactly three divisors.
 
"""

def exactly3Divisors(N):
    def divCount(n): 
        # sieve method for 
        # prime calculation 
        hh = [1] * (n + 1); 
          
        p = 2; 
        while((p * p) < n): 
            if (hh[p] == 1): 
                for i in range((p * 2), n, p): 
                    hh[i] = 0; 
            p += 1; 
      
        # Traversing through  
        # all prime numbers 
        total = 1; 
        for p in range(2, n + 1): 
            if (hh[p] == 1): 
      
                # calculate number of divisor 
                # with formula total div =  
                # (p1+1) * (p2+1) *.....* (pn+1) 
                # where n = (a1^p1)*(a2^p2)....  
                # *(an^pn) ai being prime divisor 
                # for n and pi are their respective  
                # power in factorization 
                count = 0; 
                if (n % p == 0): 
                    while (n % p == 0): 
                        n = int(n / p); 
                        count += 1; 
                    total *= (count + 1); 
                      
        return total;
    countD=0
    for I in range(1,N+1):
        if divCount(I)==3:
            countD += 1
    return (countD)
    
if __name__ == '__main__':
    T = int(input())
    for tcase in range(T):
        N = int(input())
        print (exactly3Divisors(N))