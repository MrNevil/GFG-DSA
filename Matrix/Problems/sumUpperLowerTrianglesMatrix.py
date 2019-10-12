{
#Initial Template for Python 3
def main():
    T=int(input())
    while(T>0):
        n=int(input())
        mat=[[0 for j in range(n)] for i in range(n)]
        line1=[int(x) for x in input().strip().split()]
        
       
        k=0
        for i in range(n):
            for j in range (n):
                mat[i][j]=line1[k]
                k+=1
       
        k=0
       
        sumTriangles(n, mat)
        
        print()
            
        
        T-=1
if __name__=="__main__":
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
#Complete this function
def sumTriangles(n, mat):
    #Your code here
    
    #Don't forget to print a new line to separate the testcase answers
    sumUpper = 0
    sumDiagnol = 0
    sumLower = 0
    for i in range(n):
        sumUpper += sum(mat[i][i:])
        sumLower += sum(mat[i][:(i+1)])
    print (" ".join([str(sumUpper),str(sumLower)]),end="")