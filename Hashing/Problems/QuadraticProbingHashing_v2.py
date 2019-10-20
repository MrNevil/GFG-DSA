{
#Initial Template for Python 3
def main():
    T=int(input())
    
    while(T>0):
        
        
        hashSize=int(input())
        sizeOfArray=int(input())
        arr=[int(x) for x in input().strip().split()]
        
        hash=[-1]*hashSize
        
        QuadraticProbing( hash, hashSize, arr, sizeOfArray)
        
        for i in hash:
            print(i,end=" ")
        print()
        T-=1
if __name__=="__main__":
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
#Complete this function
def QuadraticProbing( hash, hashSize, arr, sizeOfArray):
    #Your code here
    for i in range(sizeOfArray):
        hashVal = arr[i]%hashSize
        if hash[hashVal] == -1:
            hash[hashVal] = arr[i]
        else:
            k = arr[i]
            for j in range(1,hashSize):
                hashVal = (k + pow(j,2))%hashSize
                if hash[hashVal] == -1:
                    hash[hashVal] = arr[i]
                    break
                else:
                    continue