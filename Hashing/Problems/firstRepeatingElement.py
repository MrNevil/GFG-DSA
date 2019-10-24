import collections
def firstRepeatingElement(arr):
    freqs = collections.Counter(arr)
    indices = []
    for a,b in freqs.items():
        if b > 1:
            indices.append(arr.index(a)+1)
    if indices:
        return min(indices)
    else:
        return -1

if __name__ == '__main__':
    t = int(input())
    for tcase in range(t):
        N = int(input())
        arr = list(map(int,input().strip().split()))
        print (firstRepeatingElement(arr))