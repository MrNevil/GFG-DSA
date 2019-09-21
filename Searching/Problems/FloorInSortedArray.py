{
#Initial Template for Python 3
import math
def main():
        T=int(input())
        while(T>0):
            
            NX=[int(x) for x in input().strip().split()]
            N=NX[0]
            X=NX[1]
            A=[int(x) for x in input().strip().split()]
            
            print(findFloor(A,N,X))
            
            T-=1
if __name__ == "__main__":
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
#Complete this function
def findFloor(A,N,X):
    #Your code here
    floors = []
    for k,v in enumerate(A):
        if v <= X:
            floors.append(k)
    if floors:
        return max(floors)
    else:
        return -1