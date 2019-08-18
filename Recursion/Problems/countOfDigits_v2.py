def countOfDigits(n,C=0):
    if n//10 == 0:
        print (C + 1)
    else:
        C += 1
        countOfDigits(n//10,C)