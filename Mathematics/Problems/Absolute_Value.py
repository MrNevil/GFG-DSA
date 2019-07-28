{
# Initial Template for Python 3
//Position this line where user code will be pasted.
def main():
    T = int(input()) #Input the number of testcases
    while(T > 0):
        I = int(input()) #input number
        print(absolute(I)) #Call function and print
        T -= 1 #Reduce number of testcases
if __name__ == "__main__":
    main()

}
''' This is a function problem.You only need to complete the function given below '''
# User function Template for python3
# Complete this function
def absolute(I):
    # Your code here
    return (abs(I))
    