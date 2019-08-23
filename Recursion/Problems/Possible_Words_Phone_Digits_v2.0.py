{
#Initial Template for Python 3
import math
def main():
    
    T=int(input())
    
    while(T>0):
        
        N=int(input())
        a=[int(x) for x in input().strip().split()]
        
        possibleWords(a,N)
        
        print()
       
        T-=1
if __name__=="__main__":
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
##Complete this function
phone = ["abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]

def printString(digits,n,string="",index=0):
    if index == n:
        print (string,end=" ")
        return
    for i in range(len(phone[digits[index]-2])):
        string += phone[digits[index]-2][i]
        printString(digits,n,string,index+1)
        string = list(string)
        string.pop()
        string = ''.join(string)
        
def possibleWords(a,N):
    printString(a,N)