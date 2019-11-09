{
#Initial Template for Python 3
def main():
    T=int(input())
    
    while(T>0):
        
        s=input()
        if isIsogram(s) is True:
            print(1)
        else:
            print(0)
        T-=1
if __name__=="__main__":
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
#Complete this function
def isIsogram(s):
    #Your code here
    import collections
    freqs = collections.Counter(s)
    if len(set(freqs.values())) == 1 and 1 in set(freqs.values()):
        return True
    else:
        return False