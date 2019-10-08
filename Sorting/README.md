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
