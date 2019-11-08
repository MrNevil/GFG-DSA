def checkRotation(s1,s2):
    if (s1[2:] + s1[:2] == s2) or (s1[-2:] + s1[:-2] == s2):
        return 1
    else:
        return 0

if __name__ == '__main__':
    t = int(input())
    for tcase in range(t):
        s1 = input()
        s2 = input()
        print (checkRotation(s1,s2))