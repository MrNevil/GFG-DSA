{
# Initial Template for Python 3
import math
def main():
    T = int(input())
    while(T > 0):
        N = int(input())
        Hanoi.moves = 0
        h = Hanoi()
        h.toh(N, 1, 3, 2)
        print(Hanoi.moves)
        T -= 1
if __name__ == "__main__":
    main()

}
''' This is a function problem.You only need to complete the function given below '''
# User function Template for python3
class Hanoi:
    moves = 0
    def toh(self, N, fromm, to, aux):
        # Your code here
        if N == 1:
            print ("move disk 1 from rod",fromm,"to rod",to)
            Hanoi.moves += 1
            return
        self.toh(N-1, fromm, aux, to)
        print ("move disk",N,"from rod",fromm,"to rod",to)
        Hanoi.moves += 1
        self.toh(N-1, aux, to, fromm)