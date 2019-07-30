# Python3 program for finding  
# number of divisor 
  
# program for finding  
# no. of divisors 

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