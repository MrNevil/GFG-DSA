{
#Initial Template for Python 3
def main():
    T=int(input())
    
    while(T>0):
        
        hashSize=int(input())
        sizeOfArray=int(input())
        arr=[int(x) for x in input().strip().split()]
        
        
        hash=[-1]*hashSize
        
        linearProbing( hash, hashSize, arr, sizeOfArray)
        
        for i in hash:
            print(i,end=" ")
        print()
        T-=1
if __name__=="__main__":
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
##Complete this function
def linearProbing( hash, hashSize, arr, sizeOfArray):
    #Your code here
    counter = 0
    for i in range(sizeOfArray):
        hashVal = arr[i]%hashSize
        if hash[hashVal] == -1:
            hash[hashVal] = arr[i]
            counter += 1
        else:
            val = hash[hashVal]
            while((hash[hashVal] !=-1) & (counter != hashSize)):
                val += 1
                hashVal = val%(hashSize)
            if counter != hashSize:
                hash[hashVal] = arr[i]
                counter += 1