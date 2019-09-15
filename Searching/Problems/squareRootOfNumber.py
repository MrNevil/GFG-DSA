{
#Initial Template for Python 3
import math
def main():
        T=int(input())
        while(T>0):
            
            x=int(input())
            
            print(floorSqrt(x))
            
            T-=1
if __name__ == "__main__":
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
#Complete this function
def floorSqrt(x): 
    #Your code here
    if str(math.sqrt(x)).split('.')[1] == '0':
        return int(math.sqrt(x))
    else:
        return math.floor(math.sqrt(x))