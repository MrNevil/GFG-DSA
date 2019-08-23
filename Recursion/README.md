# What is Recursion:  
  
The process in which a function calls itself directly or indirectly is called recursion and the corresponding function is  
called as recursive function. Using recursive algorithm, certain problems can be solved quite easily. Examples of such problems are Towers of Hanoi (TOH), Inorder/Preorder/Postorder Tree Traversals, DFS of Graph, etc.  

## What is Base condition in recursion?
  
In recursive program, the solution to base case is provided and solution of bigger problem is expressed in terms of smaller 
problems.  
```
int fact(int n)
{
    if (n < = 1) // base case
        return 1;
    else    
        return n*fact(n-1);    
}
```  
In the above example, base case for n < = 1 is defined and larger value of number can be solved by converting to smaller one 
till base case is reached.  

## How a particular problem is solved using recursion?

The idea is represent a problem in terms of one or more smaller problems, and add one or more base conditions that stop   recursion. For example, we compute factorial n if we know factorial of (n-1). Base case for factorial would be n = 0.   
We return 1 when n = 0.  

**Why Stack Overflow error occurs in recursion?**: If base case is not reached or not defined, then stack overflow problem may arise. Let us take an example to understand this.  
```
int fact(int n)
{
    // wrong base case (it may cause
    // stack overflow).
    if (n == 100) 
        return 1;

    else
        return n*fact(n-1);
}
```  
If fact(10) is called, it will call fact(9), fact(8), fact(7) and so on but number will never reach 100. So, the base case is not reached. If the memory is exhausted by these functions on stack, it will cause stack overflow error.  

## How memory is allocated to different function calls in recursion?  

When any function is called from main(), the memory is allocated to it on stack. A recursive function calls itself, the   memory for called function is allocated on top of memory allocated to calling function and different copy of local variables is created for each function call. When the base case is reached, the function returns its value to the function by whom it is called and memory is de-allocated and the process continues.  

Let us take the example how recursion works by taking a simple function:  
```
void printFun(int test)
{
    if (test < 1)
        return;
    else
    {
        print test;
        printFun(test-1);    // statement 2
        print test;
        return;
    }
}

// Calling function printFun()
int test = 3;
printFun(test);
```  
```
Output:
3 2 1 1 2 3
```
When printFun(3) is called from main(), memory is allocated to printFun(3) and a local variable test is initialized to 3 and statement 1 to 4 are pushed on the stack as shown in below diagram. It first prints ‘3’. In statement 2, printFun(2) is called and memory is allocated to printFun(2) and a local variable test is initialized to 2 and statement 1 to 4 are pushed in the stack. Similarly, printFun(2) calls printFun(1) and printFun(1) calls printFun(0). printFun(0) goes to if statement and it return to printFun(1). Remaining statements of printFun(1) are executed and it returns to printFun(2) and so on. In the output, value from 3 to 1 are printed and then 1 to 3 are printed.  

## Disadvantage of Recursion:  
Note that both recursive and iterative programs have same problem solving powers, i.e., every recursive program can be written iteratively and vice versa is also true. Recursive program has greater space requirements than iterative program as all functions will remain in stack until base case is reached. It also has greater time requirements because of function calls and return overhead.  

## Advantages of Recursion:  
Recursion provides a clean and simple way to write code. Some problems are inherently recursive like tree traversals, Tower of Hanoi, etc. For such problems it is preferred to write recursive code. We can write such codes also iteratively with the help of stack data structure.  

# Basic problems on Recursion:  
### Problem - 1:  

Given an unsorted array of N elements and an element X. The task is to write a recursive function to check whether the element X is present in the given array or not.  

Example:  
```
array[] = {1, 2, 3, 4, 5}
X = 3.

The function should return True, as 3 is 
present in the array.
```
**Solution:** The idea is to compare the first element of the array with X. If the element matches with X then return True otherwise recur for the remaining part of the array.  

The recursive function will somewhat look like as shown below:  
```
// arr[] is the given array 
// l is the lower bound in the array
// r is the upper bound
// x is the element to be searched for
// l and r defines that search will be 
// performed between indices l to r

bool recursiveSearch(int arr[], int l,  
                            int r, int x) 
{ 
    if (r < l) 
        return false; 
    if (arr[l] == x) 
        return true; 
    if (arr[r] == x) 
        return true; 

    return recursiveSearch(arr, l + 1,  
                              r - 1, x); 
} 
```
Time Complexity: The above algorithm runs in O(N) time where, N is the number of elements present in the array.  
Space Complexity: There is no extra space used however the internal stack takes O(N) extra space for recursive calls.  

### Problem - 2:  

Given a string, the task is to write a recursive function to check if the given string is palindrome or not.  

```
Examples:
Input : string = "malayalam"
Output : Yes
Reverse of malayalam is also
malayalam.

Input : string = "max"
Output : No
Reverse of max is not max.
```

**Solution:** The idea to write the recursive function is simple and similar to the above problem:  
If there is only one character in string, return true.  
Else compare first and last characters and recur for remaining substring.  

Recursive Function:  
```
// s and e defines the start and end index of string

bool isPalindrome(char str[], int s, int e) 
{ 
    // If there is only one character 
    if (s == e) 
        return true; 
  
    // If first and last 
    // characters do not match 
    if (str[s] != str[e]) 
        return false; 
  
    // If there are more than  
    // two characters, check if  
    // middle substring is also  
    // palindrome or not
    if (s < e) 
        return isPalindrome(str, s + 1, e - 1); 
  
    return true; 
} 
```  

# Tail Recursion:  
As we read before, that recursion is defined when a function invokes/calls itself.  

**Tail Recursion:** A recursive function is said to be following Tail Recursion if it invokes itself at the end of the function. That is, if all of the statements are executed before the function invokes itself then it is said to be following Tail Recursion.  

For Example:  
```
// This is a Tail Recursion

void printN(int N)
{
    if(N==0)
        return;
    else
        cout<<N<<" ";
    
    printN(N-1);
}
```
The above function call for N = 5 will print:  
```
5 4 3 2 1
```

### Which one is Better-Tail Recursive or Non Tail-Recursive?  

The tail-recursive functions are considered better than non-tail recursive functions as tail-recursion can be optimized by compiler. The idea used by compilers to optimize tail-recursive functions is simple, since the recursive call is the last statement, there is nothing left to do in the current function, so saving the current function’s stack frame is of no use.  


### Can a non-tail recursive function be written as tail-recursive to optimize it?  

Consider the following function to calculate factorial of N. It is a non-tail-recursive function. Although it looks like a tail recursive at first look. If we take a closer look, we can see that the value returned by fact(N-1) is used in fact(N), so the call to fact(N-1) is not the last thing done by fact(N).  

```
int fact(int N) 
{ 
    if (N == 0) 
        return 1; 
  
    return N*fact(N-1); 
}  
```

The above function can be written as a tail recursive function. The idea is to use one more argument and accumulate the factorial value in second argument. When N reaches 0, return the accumulated value.  

```
int factTR(int N, int a)
{ 
    if (N == 0)  
        return a; 
  
    return factTR(N-1, N*a); 
} 
```

## Maximum number of pieces of a rope problem using Recursion:  

Problem: Given a rope of length n, and three-piece lengths a, b and c. We need to find the maximum number of pieces we can make of the rope such that the length of every piece is in {a, b, c}.  

```
Examples : 
Input : n = 5, a = 1, b = 2, c = 3
Output : 5
We make 5 pieces each of length 1.

Input : n = 23, a = 11, b = 9, c = 12
Output : 2
We make 2 pieces lengths 11 and 12.
```
The idea is to consider every possibility using recursion. We consider all three choices for the first cut. Recursively compute number of pieces for every choice. If none of the choices lead to a solution, we return -1. Otherwise, we return the maximum.  

C++ Code:  
```
// CPP program to find maximum number of
// pieces of a rope
#include <bits/stdc++.h>
using namespace std;
int maxCuts(int n, int a, int b, int c)
{
    if (n < 0)
        return -1;
    if (n == 0)
        return 0;
    int res = max({ maxCuts(n - a, a, b, c),
                    maxCuts(n - b, a, b, c),
                    maxCuts(n - c, a, b, c) });
    if (res == -1)
        return -1;
    else
        return res + 1;
}

int main()
{
    cout << maxCuts(23, 11, 9, 12);
    return 0;
}
```
Java Code:  
```
import java.io.*;

public class GFG {

    static int maxCuts(int n, int a, int b, int c)
    {
        if (n < 0)
            return -1;
        if (n == 0)
            return 0;
        int res = Math.max(maxCuts(n - a, a, b, c),
                    Math.max(maxCuts(n - b, a, b, c),
                           maxCuts(n - c, a, b, c)));
        if (res == -1)
            return -1;
        else
            return res + 1;
    }

    public static void main(String[] args)
    {
        int n = 23, a = 12, b = 9, c = 11;
        System.out.println(maxCuts(n, a, b, c));
    }
}
```
For n = 23, we make three recursive calls for 23-9, 23-11 and 23-12 which are for 14, 12 and 11 respectively.  

Each of these 3 makes three recursive calls. 14 makes three recursive calls for 14-9, 14-11 and 14-12.  

Similarly, 12 and 11 make three recursive calls. This keeps on going until we reach either 0 or negative value.  

```
                                     23
                /                    |              \
             14                      12             11
           /     |     \           /  |   \         / | \
         5      3       2         4   1   0       2  0  -1
      /|\       /|\    /|\       /|\ /|\         /|\ 
    All -ve  All -ve  All-ve     All -ve         All -ve

-ve means negative
```
Note that all values at leaves are negative and they will return -1. So, parents of all -ve will return -1. So you get -1 from the first recursive call for 14. From second and third recursive calls you get 1. You add 1 to it and return 2.  

## Subset Generation Problem:  

Given a set represented as string, write a recursive code to print all subsets of it. The subsets can be printed in any order.  
```
Examples:
Input :  set = "abc"
Output : "". "a", "b", "c", "ab", "ac", "bc", "abc"

Input : set = "abcd"
Output : "" "a" "ab" "abc" "abcd" "abd" "ac" "acd"
         "ad" "b" "bc" "bcd" "bd" "c" "cd" "d"
```

The idea is to consider two cases for every character. (i) Consider current character as part of current subset (ii) Do not consider current character as part of current subset.  

C++ Code:  
```
// CPP program to generate power set
#include <bits/stdc++.h>
using namespace std;

// str : Stores input string
// curr : Stores current subset
// index : Index in current subset, curr
void powerSet(string str, int index = 0,
              string curr = "")
{
    int n = str.length();

    // base case
    if (index == n) {
        cout << curr << endl;
        return;
    }

    // Two cases for every character
    // (i) We consider the character
    // as part of current subset
    // (ii) We do not consider current
    // character as part of current
    // subset
    powerSet(str, index + 1, curr + str[index]);
    powerSet(str, index + 1, curr);
}

// Driver code
int main()
{
    string str = "abc";
    powerSet(str);
    return 0;
}
```

Java Code:  
```
// Java program to generate power set
class GFG {

// str : Stores input string 
// curr : Stores current subset 
// index : Index in current subset, curr 
static void powerSet(String str, int index, 
            String curr) 
    
{ 
    int n = str.length(); 

    // base case 
    if (index == n)
    { 
        System.out.println(curr);
        return; 
    } 

    // Two cases for every character 
    // (i) We consider the character 
    // as part of current subset 
    // (ii) We do not consider current 
    // character as part of current 
    // subset 
    powerSet(str, index + 1, curr + str.charAt(index)); 
    powerSet(str, index + 1, curr);
} 

// Driver code 
public static void main(String[] args) 
{
    String str = "abc"; 
        int index = 0;
        String curr="";
    powerSet(str,index,curr); 

    }
}
```
Output:  
```
abc
ab
ac
a
bc
b
c
```
Let us understand the recursion with an example "abc". Every node in below tree represents string curr.  
```
                  curr=""
               /         \
            "a"             ""
           /   \           /    \
        "ab"    "a"       "b"    ""
       /  \     /  \     /  \    / \
   "abc" "ab" "ac" "a" "bc" "b" "c"  ""
```

At root, index = 0.
At next level of tree index = 1
At third level, index = 2
At fourth level index = 3 (becomes equal to string length), so we print the subset.

