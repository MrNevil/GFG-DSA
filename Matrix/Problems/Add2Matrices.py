{
#Initial Template for Python 3
def main():
    T=int(input())
    while(T>0):
        n1,m1=map(int,input().strip().split())
        arr1=[[0 for j in range(m1)] for i in range(n1)]
        line1=[int(x) for x in input().strip().split()]
        
       
        k=0
        for i in range(n1):
            for j in range (m1):
                arr1[i][j]=line1[k]
                k+=1
       
        k=0
       
        n2,m2=map(int,input().strip().split())
        arr2=[[0 for j in range(m2)] for i in range(n2)]
        line2=[int(x) for x in input().strip().split()]
        
       
        k=0
        for i in range(n2):
            for j in range (m2):
                arr2[i][j]=line2[k]
                k+=1
       
        k=0
       
       
       
        sumMatrix(n1, m1, n2, m2, arr1, arr2)
        print() 
        
        T-=1
if __name__=="__main__":
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
'''
  Function to find sum of matrices
  n1, m1, n2, m2: rows and columns of matrices respectively
  arr1[][], arr2[][]: two input matrices
'''
def sumMatrix(n1, m1, n2, m2, arr1, arr2):
    #Your code here
    if n1!=n2 or m1!=m2:
        print (-1,end = " ")
    elif n1==n2 and m1==m2:
        tmp = [[0]*m1 for i in range(n1)]
        for r in range(n1):
            for c in range(m1):
                tmp[r][c] = arr1[r][c] + arr2[r][c]
        for r in tmp:
            print (" ".join(str(h) for h in r),end = " ")