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
        exchangeColumns(n, m, mat)
       
        print()
            
        
        T-=1
if __name__=="__main__":
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
#arr1 is matrix
#n1,m1 are dimension
def exchangeColumns(n1, m1, arr1):
    #Your code here
    tmp = 0
    for i in range(n1):
        tmp = arr1[i][0]
        arr1[i][0] = arr1[i][m1-1]
        arr1[i][m1-1] = tmp
    for r in arr1:
        print (" ".join(str(h) for h in r),end=" ")