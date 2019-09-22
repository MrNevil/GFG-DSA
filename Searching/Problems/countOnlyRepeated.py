import collections
def countRepeated(arr,n):
    freqs = collections.Counter(arr)
    x = [(k,v) for k,v in freqs.items() if v > 1]
    return " ".join([str(x[0][0]),str(x[0][1])])

if __name__ == '__main__':
    T = int(input())
    for tc in range(T):
        N = int(input())
        arr = list(map(int,input().strip().split()))
        print (countRepeated(arr,N))