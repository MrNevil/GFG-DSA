def sortString(st):
    x = sorted(st)
    return "".join(x)
    
if __name__ == '__main__':
    t = int(input())
    for c in range(t):
        n = int(input())
        st = input()
        print (sortString(st))