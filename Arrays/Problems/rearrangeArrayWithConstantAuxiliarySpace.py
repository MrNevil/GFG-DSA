{
#Initial Template for Python 3
import math
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            arrange(arr,n)
            
            for i in arr:
                print(i,end=" ")
            
            print()
            
            T-=1
if __name__ == "__main__":
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
##Complete this code
def arrange(arr, n): 
    #Your code here
    for i in range(n):
        arr.append(arr[arr[i]])
    arr[:] = arr[n:]