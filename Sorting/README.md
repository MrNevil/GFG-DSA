# Introduction to Sorting:  
  
**Sorting** any sequence means to arrange the elements of that sequence according to some specific criterion.  

For Example, the array arr[] = {5, 4, 2, 1, 3} after sorting in increasing order will be: arr[] = {1, 2, 3, 4, 5}. The same array after sorting in descending order will be: arr[] = {5, 4, 3, 2, 1}.  

**In-Place Sorting:** An in-place sorting algorithm uses constant extra space for producing the output (modifies the given array only). It sorts the list only by modifying the order of the elements within the list.  

In this tutorial, we will see three of such in-place sorting algorithms, namely:  
+ Insertion Sort  
+ Selection Sort  
+ Bubble Sort  

## Insertion Sort:  
  
Insertion Sort is an In-Place sorting algorithm. This algorithm works in a similar way of sorting a deck of playing cards.  

The idea is to start iterating from the second element of array till last element and for every element insert at its correct position in the subarray before it.  

In the below image you can see, how the array [4, 3, 2, 10, 12, 1, 5, 6] is being sorted in increasing order following the insertion sort algorithm.  
  
![Insertion Sort](https://github.com/absognety/DSA-GeeksClasses/blob/master/Sorting/insertionsort.png "insertion sort")  
  
### Algorithm:  
```
Step 1: If the current element is 1st element of array, 
        it is already sorted.
Step 2: Pick next element
Step 3: Compare the current element will all elements 
        in the sorted sub-array before it.
Step 4: Shift all of the elements in the sub-array before 
        the current element which are greater than the current 
        element by one place and insert the current element 
        at the new empty space.
Step 5: Repeat step 2-3 until the entire array is sorted.
```  
**Another Example:**  
arr[] = {12, 11, 13, 5, 6}

Let us loop for i = 1 (second element of the array) to 4 (Size of input array - 1).  
+ i = 1, Since 11 is smaller than 12, move 12 and insert 11 before 12.
11, 12, 13, 5, 6  
+ i = 2, 13 will remain at its position as all elements in A[0..I-1] are smaller than 13
11, 12, 13, 5, 6  
+ i = 3, 5 will move to the beginning and all other elements from 11 to 13 will move one position ahead of their current position 5, 11, 12, 13, 6  
+ i = 4, 6 will move to position after 5, and elements from 11 to 13 will move one position ahead of their current position.
5, 6, 11, 12, 13  
  
### Function Implementation:  
```

/* Function to sort an array using insertion sort*/
void insertionSort(int arr[], int n) 
{ 
   int i, key, j; 
   for (i = 1; i < n; i++) 
   { 
       key = arr[i]; 
       j = i-1; 
  
       /* Move elements of arr[0..i-1], that are 
          greater than key, to one position ahead 
          of their current position */
       while (j >= 0 && arr[j] > key) 
       { 
           arr[j+1] = arr[j]; 
           j = j-1; 
       } 
       arr[j+1] = key; 
   } 
}
```  
**Time Complexity: O(N2), where N is the size of the array.**  
