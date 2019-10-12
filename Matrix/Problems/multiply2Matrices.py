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
       
       
       
        multiplyMatrix(n1, m1, n2, m2, arr1, arr2)
        
        print()
            
        
        T-=1
if __name__=="__main__":
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
#Complete this function
def multiplyMatrix(n1, m1, n2, m2, arr1, arr2): 
  #Your code here
  if m1!=n2:
      print (-1,end = "")
  else:
      result = [[0]*m2 for i in range(n1)]
      for i in range(n1):
          for j in range(m2):
              for k in range(m1):
                  result[i][j] += arr1[i][k] * arr2[k][j]
  for i in range(n1):
      for j in range(m2):
          print (result[i][j],end=" ")