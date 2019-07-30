{
#Initial Template for Python 3
import atexit
import io
import sys
# Contributed by : Nagendra Jha
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        a,b = map(int,input().strip().split())
        print(multiplicationUnderModulo(a,b))

}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
def multiplicationUnderModulo(a,b):
    '''
    :param a: given value of a
    :param b: given value of b
    :return: Integer , sum under modulo
    '''   
    M = 1000000007
    # code here
    return ((a*b)%M)