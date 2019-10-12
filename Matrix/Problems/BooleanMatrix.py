{
#Initial Template for Python 3
def main():
    T=int(input())
    while(T>0):
        r,c=map(int,input().split())
        
        
        mat=[]
        for i in range(r):
            line=[int(x) for x in input().strip().split()]
            mat.append(line)
        booleanMatrix(r, c, mat)
        
        T-=1
if __name__=="__main__":
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
#r is rows
#c is cols
#mat is matrx
#print it in this function after modifying it
def booleanMatrix(r, c, mat):
    #Your code here
    tmp = [[0]*c for i in range(r)]
    for row in range(r):
        if 1 in mat[row]:
            #count1 = row.count(1)
            for ind,val in enumerate(mat[row]):
                if val == 1:
                    for rw in range(r):
                        tmp[rw][ind] = 1
            tmp[row] = [1]*c
    for i in tmp:
        print (" ".join(str(h) for h in i))