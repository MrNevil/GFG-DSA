# Introduction to Arrays:  
  
An array is a collection of items of same data type stored at contiguous memory locations. This makes it easier to calculate the position of each element by simply adding an offset to a base value, i.e., the memory location of the first element of the array (generally denoted by the name of the array).  

For simplicity, we can think of an array a fleet of stairs where on each step is placed a value (let’s say one of your friends). Here, you can identify the location of any of your friends by simply knowing the count of the step they are on.  

**Remember:** “Location of next index depends on the data type we use”.  

![Array-1](https://github.com/absognety/DSA-GeeksClasses/blob/master/Arrays/array-1.png "Array 1")  

The above image can be looked as a top-level view of a staircase where you are at the base of staircase. Each element can be uniquely identified by their index in the array (in a similar way as you could identify your friends by the step on which they were on in the above example).  

Defining an Array: Array definition are similar to defining any other variable. There are two things need to be kept in mind, data type of the array elements and the size of the array. The size of the array is fixed and the memory for an array needs to be allocated before use, size of an array cannot be increased or decreased dynamically.  

Generally, arrays are declared as:  

```
dataType arrayName[arraySize];

An array is distinguished from a normal variable 
by brackets [ and ].
```  

**Accessing array elements:** Arrays allows to access elements randomly. Elements in an array can be accessed using indexes. Suppose an array named arr stores N elements. Indexes in an array are in the range of 0 to N-1, where the first element is present at 0-th index and consecutive elements are placed at consecutive indexes. Element present at ith index in the array arr[] can be accessed as arr[i].  

Below image shows an array arr[] of size 5:  

![Array-2](https://github.com/absognety/DSA-GeeksClasses/blob/master/Arrays/Array-2.jpg "Array 2")  

## Advantages of using arrays:  
+ Arrays allow random access of elements. This makes accessing elements by position faster.  
+ Arrays have better cache locality that can make a pretty big difference in performance.  

```
Examples:
// A character array in C/C++/Java

char arr1[] = {'g', 'e', 'e', 'k', 's'};



// An Integer array in C/C++/Java

int arr2[] = {10, 20, 30, 40, 50};



// Item at i'th index in array is typically accessed

// as "arr[i]".  For example arr1[0] gives us 'g'

// and arr2[3] gives us 40.
```  
## Searching in an Array

Searching an element in an array means to check if a given element is present in an array or not. This can be done by accessing elements of the array one by one starting from the first element and checking if any of the element matches with the given element.  

We can use loops to perform the above operation of array traversal and access the elements using indexes.  

Suppose the array is named arr[] with size N and the element to be searched is referred as key. Below is the algorithm to perform to the search operation in the given array.  

```
for(i = 0; i < N; i++)
{
    if(arr[i] == key)
    { 
        print "Element Found";
    }
    else
    {
        print "Element not Found";
    }
}
```
**Time Complexity** of this search operation will be O(N) in the worst case as we are checking every element of the array from 1st to last, so the number of operations is N.  


# Insertion and Deletion in Arrays:  
## Insertion in Arrays
Given an array of a given size. The task is to insert a new element in this array. There are two possible ways of inserting elements in an array:  
+ Insert elements at the end of the array.  
+ Insert element at any given index in the array.  

**Special Case:** A special case is needed to be considered is that whether the array is already full or not. If the array is full, then the new element can not be inserted.  

Consider the given array is arr[] and the initial size of the array is N, that is the array can contain a maximum of N elements and the length of the array is len. That is, there are len number of elements already present in this array.

**Insert an element K at end in arr[]:** The first step is to check if there is any space left in the array for new element. To do this check,  
```
if(len < N)
     // space left
else
     // array is full
```
If there is space left for the new element, insert it directly at the end at position `len + 1` and index `len`:  
```
arr[len] = k;
```

**Time Complexity** of this insert operation is constant, i.e. O(1) as we are directly inserting the element in a single operation.  

**Insert an element K at position, pos in arr[]:** The first step is to check if there is any space left in the array for new element. To do this check,  
```
if(len < N)
     // space left
else
     // array is full
```
Now, if there is space left, the element can be inserted. The index of the new element will be `idx = pos - 1.`  

Now, before inserting the element at the index idx, shift all elements from the index idx till end of the array to the right by 1 place. This can be done as:  
```
for(i = len-1; i >= idx; i--)
{
    arr[i+1] = arr[i];
}
```
After shifting the elements, place the element K at index idx.  
```
arr[idx] = K;
```
**Time Complexity** in worst case of this insertion operation can be linear i.e. O(N) as we might have to shift all of the elements by one place to the right.  

## Deletion in Arrays:  

To delete a given element from an array, we will have to first search the element in the array. If the element is present in the array then delete operation is performed for the element otherwise the user is notified that the array does not contains the given element.  

Consider the given array is arr[] and the initial size of the array is N, that is the array can contain a maximum of N elements and the length of the array is len. That is, there are len number of elements already present in this array.  

**Deleting an element K from the array arr[]:** Search the element K in the array arr[] to find the index at which it is present.  

```
for(i = 0; i < N; i++)
{
    if(arr[i] == K)
        idx = i; return;
    else
        Element not Found;
}
```  

Now, to delete the element present at index idx, left shift all of the elements present after idx by one place and finally reduce the length of the array by 1.  

```
for(i = idx+1; i < len; i++)
{
    arr[i-1] = arr[i];
}

len = len-1;
```
**Time Complexity** in worst case of this insertion operation can be linear i.e. O(N) as we might have to shift all of the elements by one place to the left.  
