{
#Initial Template for Python 3
import math
def main():
        T=int(input())
        while(T>0):
            
            hashSize=int(input())
            sizeOfArray=int(input())
            arr=input().strip()
            arr=arr.split()
            arr=list(map(int,arr))
            
            hashTable=[0]*hashSize
            
            for i in range(hashSize):
                hashTable[i]=[]
            
            separateChaining( hashTable, hashSize, arr, sizeOfArray)
            
            
            for i in range(len(hashTable)):
                if len(hashTable[i])>0:
                    print(str(i)+"->",end="")
                    for j in range(len(hashTable[i])-1):
                        print(str(hashTable[i][j])+"->",end="")
                    print(hashTable[i][len(hashTable[i])-1],end="")
                    print()
            T-=1
if __name__ == "__main__":
    main()

}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
#Complete this code
def separateChaining( hashTable, hashSize, arr, sizeOfArray):
    #Your code here
    for i in range(len(arr)):
        hashVal = arr[i]%hashSize
        hashTable[hashVal].append(arr[i])