# Theory on Arrays:  
  
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
