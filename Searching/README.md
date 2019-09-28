# Linear Search:  
  
**Linear Search** means to sequentially traverse a given list or array and check if an element is present in the respective array or list. The idea is to start traversing the array and compare elements of the array one by one starting from the first element with the given element until a match is found or end of the array is reached.  

![Linear-Search](https://github.com/absognety/DSA-GeeksClasses/blob/master/Searching/Linear-Search.png "Linear Search")  

#### Examples:  
```
Input : arr[] = {10, 20, 80, 30, 60, 50, 
                     110, 100, 130, 170}
          key = 110;
Output : 6
Element 110 is present at index 6

Input : arr[] = {10, 20, 80, 30, 60, 50, 
                     110, 100, 130, 170}
           key = 175;
Output : -1
Element 175 is not present in arr[].
```  
**Problem:** Given an array arr[] of N elements, write a function to search a given element X in arr[].  

**Algorithm:**  
+ Start from the leftmost element of arr[] and one by one compare X with each element of arr[].  
+ If X matches with an element, return the index.  
+ If X doesn’t match with any of elements and end of the array is reached, return -1.  

**Function:**  
```
// Function to linearly search the element X in the 
// array arr[] of N elements
int search(int arr[], int N, int X) 
{    
    // Pointer to traverse the array
    int i; 

    // Start traversing the array
    for (i = 0; i < N; i++) 
    {   
        // If a successful match is found,
        // return the index
        if (arr[i] == X) 
            return i; 
    }

    // If the element is not found,
    // and end of array is reached
    return -1; 
} 
```  
**Time Complexity:** O(N). Since we are traversing the complete array, so in worst case when the element X does not exists in the array, number of comparisons will be N. Therefore, worst case time complexity of the linear search algorithm is O(N).  

# Binary Search:  
  
**Binary Search** is a searching algorithm for searching an element in a sorted list or array. Binary Search is efficient than Linear Search algorithm and performs the search operation in logarithmic time complexity for sorted arrays or lists.  

Binary Search performs the search operation by repeatedly dividing the search interval in half. The idea is to begin with an interval covering the whole array. If the value of the search key is less than the item in the middle of the interval, narrow the interval to the lower half. Otherwise narrow it to the upper half. Repeatedly check until the value is found or the interval is empty.  
  
![Binary Search](https://github.com/absognety/DSA-GeeksClasses/blob/master/Searching/Binary-Search.png "Binary Search")  

**Problem:** Given a sorted array arr[] of N elements, write a function to search a given element X in arr[] using Binary Search Algorithm.  

**Algorithm:** We basically ignore half of the elements just after one comparison.  
+ Compare X with the middle element of the array.  
+ If X matches with middle element, we return the mid index.  
+ Else If X is greater than the mid element, then X can only lie in right half subarray after the mid element. So we will now look for X in only the right half ignoring the complete left half.  
+ Else if X is smaller, search for X in the left half ignoring the right half.  

**Implementation:** The Binary Search algorithm can be implemented both recursively and iteratively.  
**Recursive Implementation:**  
```
// otherwise -1 

// Initially,
// l = 0, first index of arr[].
// r = N-1, last index of arr[].
int binarySearch(int arr[], int l, int r, int x) 
{ 
    if (r >= l) { 
        int mid = l + (r - l) / 2; 
  
        // If the element is present at the middle 
        // itself 
        if (arr[mid] == x) 
            return mid; 
  
        // If element is smaller than mid, then 
        // it can only be present in left subarray 
        if (arr[mid] > x) 
            return binarySearch(arr, l, mid - 1, x); 
  
        // Else the element can only be present 
        // in right subarray 
        return binarySearch(arr, mid + 1, r, x); 
    } 
  
    // We reach here when element is not 
    // present in array 
    return -1; 
} 
```  
**Iterative Implementation:**  
```
// A iterative binary search function. It returns 
// location of x in given array arr[l..r] if present, 
// otherwise -1 

// Initially,
// l = 0, first index of arr[].
// r = N-1, last index of arr[].
int binarySearch(int arr[], int l, int r, int x) 
{ 
    while (l <= r) { 
        int m = l + (r - l) / 2; 
  
        // Check if x is present at mid 
        if (arr[m] == x) 
            return m; 
  
        // If x greater, ignore left half 
        if (arr[m] < x) 
            l = m + 1; 
  
        // If x is smaller, ignore right half 
        else
            r = m - 1; 
    } 
  
    // if we reach here, then element was 
    // not present 
    return -1; 
}
```  
**Time Complexity:** O(Log N), where N is the number of elements in the array.  

# Ternary Search:  
  
**Ternary Search** is a Divide and Conquer Algorithm used to perform search operation in a sorted array. This algorithm is similar to the Binary Search algorithm but rather than dividing the array into two parts, it divides the array into three equal parts.

In this algorithm, the given array is divided into three parts and the key (element to be searched) is compared to find the part in which it lies and that part is further divided into three parts.

We can divide the array into three parts by taking mid1 and mid2 which can be calculated as shown below. Initially, l and r will be equal to 0 and N-1 respectively, where N is the length of the array.

```
mid1 = l + (r-l)/3
mid2 = r – (r-l)/3
```  
