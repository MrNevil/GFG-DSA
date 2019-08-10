# What is Recursion:  
  
The process in which a function calls itself directly or indirectly is called recursion and the corresponding function is  
called as recursive function. Using recursive algorithm, certain problems can be solved quite easily. Examples of such problems  
are Towers of Hanoi (TOH), Inorder/Preorder/Postorder Tree Traversals, DFS of Graph, etc.  

# What is Base condition in recursion?
  
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
