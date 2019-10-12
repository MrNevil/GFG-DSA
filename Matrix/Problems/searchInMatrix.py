{
#Initial Template for Python 3
def main():
    T=int(input())
    while(T>0):
        n,m=map(int,input().split())
        mat=[[0 for j in range(m)] for i in range(n)]
        line1=[int(x) for x in input().strip().split()]
        x=int(input())
       
        k=0
        for i in range(n):
            for j in range (m):
                mat[i][j]=line1[k]
                k+=1
       
        print(search(n, m, mat,x))
        T-=1
if __name__=="__main__":
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
#mat is matrix
#n1 is rows
#m1 is cols
#x is element to search
def search(n1, m1, mat, x):
    #Your code here
    r = 0
    while r <= n1-1:
        if x in mat[r]:
            return 1
        else:
            r += 1
    return 0