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
                
        print(findMinOpeartion(mat,n))
        
            
        
        T-=1
if __name__=="__main__":
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
#Complete this function and return count
def findMinOpeartion(matrix, n):
    #Your code here
    maxs,maxcolSum = 0,0
    totalSum = 0
    for i in range(n):
        currentRSum = 0
        for j in range(n):
            currentRSum += matrix[i][j]
        totalSum += currentRSum
        if maxs < currentRSum:
            maxs = currentRSum
    for i in range(n):
        currentCSum = 0
        for j in range(n):
            currentCSum += matrix[j][i]
        if maxs < currentCSum:
            maxs = currentCSum
    return (maxs * n) - totalSum