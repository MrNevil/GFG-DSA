{
#Initial Template for Python 3
def main():
    T=int(input())
    while(T>0):
        n,m=map(int,input().split())
        mat=[[0 for j in range(m)] for i in range(n)]
        line1=[int(x) for x in input().strip().split()]
        
       
        k=0
        for i in range(n):
            for j in range (m):
                mat[i][j]=line1[k]
                k+=1
       
        k=0
        
        n,m=m,n
        spirallyTraverse(m,n,mat)
        
        
        print()
        
            
        
        T-=1
if __name__=="__main__":
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
#Complete this function
#a is the matrix
#m is rows
#n is cols
def spirallyTraverse(m, n, a) : 
    #Your code here
    k = 0; l = 0
    while (k < m and l < n) : 
        for i in range(l, n) : 
            print(a[k][i], end = " ") 
        k += 1
        
        for i in range(k, m) : 
            print(a[i][n - 1], end = " ") 
        n -= 1
        
        if ( k < m) : 
            for i in range(n - 1, (l - 1), -1) : 
                print(a[m - 1][i], end = " ") 
            m -= 1
            
        if (l < n) : 
            for i in range(m - 1, k - 1, -1) : 
                print(a[i][l], end = " ") 
            l += 1