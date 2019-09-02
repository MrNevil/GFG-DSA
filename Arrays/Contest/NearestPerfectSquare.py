import math
def nearPerfectSq(x):
    sqr = math.sqrt(x)
    if str(sqr).split('.')[1]=='0':
        p,q = int(sqr)-1,int(sqr)+1
        diffp,diffq = abs(p**2 - x),abs(q**2 - x)
        if min(diffp,diffq) == diffp:
            return p**2
        else:
            return q**2
    a,b = math.floor(sqr),math.ceil(sqr)
    sqa,sqb = a**2,b**2
    if abs(sqa-x) == abs(sqb-x):
        return max(sqa,sqb)
    else:
        minD = min(abs(sqa-x),abs(sqb-x))
        if minD == abs(sqa-x):
            return sqa
        else:
            return sqb


if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        x = int(input())
        print (nearPerfectSq(x))