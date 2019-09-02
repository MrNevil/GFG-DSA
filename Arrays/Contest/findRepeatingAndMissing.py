import collections
def getTheShadow(arr,n):
    repNums = []
    freqs = collections.Counter(arr)
    for k,v in freqs.items():
        if v == 2:
            repNums.append(k)
    for i in range(n):
        if arr[abs(arr[i])-1]> 0:
            arr[abs(arr[i])-1] = -arr[abs(arr[i])-1]
    missNums = []
    for i in range(n):
        if arr[i] > 0:
            missNums.append(i+1)
    return ' '.join([str(repNums[0]),str(missNums[0])])

if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        n = int(input())
        arr = list(map(int,input().strip().split()))
        print (getTheShadow(arr,n))