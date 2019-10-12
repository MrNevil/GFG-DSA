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
       
        printS(mat,n)
        print()
            
        
        T-=1
if __name__=="__main__":
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
#Complete this function
def printS(mat,n): 
   #Your code here
   for i in range(n):
       if i%2 == 0:
           print (" ".join(str(f) for f in mat[i]),end = " ")
       else:
           print (" ".join(str(f) for f in mat[i][::-1]),end = " ")