import operator
def positiveNegativePairs(arr,n):
    if len(set(arr)) == 1 and 0 in arr:
        return 0
    mydict = {}
    for i in range(n):
        if arr[i] > 0:
            x = -1 * arr[i]
            if x in arr:
                mydict[arr[i]] = x
            else:
                continue
        elif arr[i] < 0:
            y = -1 * arr[i]
            if y in arr:
                mydict[y] = arr[i]
            else:
                continue
        else:
            continue
    if mydict:
        res = []
        f = sorted(mydict.items(),key=operator.itemgetter(0))
        for v in f:
            res.extend(list(v))
        return (" ".join(str(i) for i in res))
    else:
        return 0
if __name__ == '__main__':
    t = int(input())
    for tcase in range(t):
        n = int(input())
        arr = list(map(int,input().strip().split()))
        print (positiveNegativePairs(arr,n))