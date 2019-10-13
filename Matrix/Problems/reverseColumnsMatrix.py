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
        reverseCol(n, m, mat)
        
        for i in range(n):
            for j in range(m):
                print(mat[i][j],end=" ")
        print()
        
            
        
        T-=1
if __name__=="__main__":
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
#arr1 is matrix
#n1 is rows
#m1 is cols
def reverseCol(n1, m1, arr1):
    #Your code here
    for i in range(n1):
        arr1[i] = arr1[i][::-1]