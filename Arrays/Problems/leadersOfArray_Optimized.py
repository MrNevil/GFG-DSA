{
#Initial Template for Python 3
import math
    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        N=int(input())
        
        A=[int(x) for x in input().strip().split()]
        
        A=leaders(A,N)
        
        for i in A:
            print(i,end=" ")
        print()
        
        T-=1
if __name__=="__main__":
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
#Complete this function
def leaders(A,N):
    #Your code here
    
    '''
    Just return the list with leaders in it
    '''
    maxx = A[::-1][0]
    leaders = [maxx]
    for i in A[::-1][1:]:
        if i >= maxx:
            maxx = i
            leaders.append(maxx)
    return leaders[::-1]