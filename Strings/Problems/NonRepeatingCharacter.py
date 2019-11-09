import collections
def nonRepeatingChar(s,n):
    freqs = collections.Counter(s)
    if 1 not in freqs.values():
        return -1
    else:
        for c in s:
            if freqs[c]==1:
                return c

if __name__ == '__main__':
    t = int(input())
    for tcase in range(t):
        n = int(input())
        s = input()
        print (nonRepeatingChar(s,n))