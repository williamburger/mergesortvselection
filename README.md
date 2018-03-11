# William Burger - Mergesort versus Selection Sort Programming Project
## 1) Source Code - See attached documents
## 2) Smaller Test cases
* How I tested: I generated a bunch of randomized arrays and calculated the median using both my mergesort and selection implementations. I compared these results to using the Python numpy library median function to ensure that they are correct. Also, when I run on larger random data sets, I always check that the merge median and selection median values are equal. See a below example of a random array tested using numpy median and my merge versus selection medians:
![](SmallTest.png)
* In the above image, since 26 is a value in the array and the value returned is 26.5, the lower median is 26 (it fell between the two values 26 and 27)

## 3) Runtime Results Graphs
* I graphed everything using Python's plotly package
* Below is the plot of runtimes between merge sort and selection for finding the median of random array sizes between 10 and 100000. 
![](Sellection_v_merge_sort.png)

* Below is the plot of Inversion ratios versus the time it takes for selection sort to determine the median of the array. This was done on arrays of different sizes in this case.
![](Inv_ratio_v_time_diff_array_size.png)

* Below is the plot of Inversion ratios versus the time it takes for selection sort to determine the median of the array. This was done with constant array size (Held at size 10000)
![](Inversion_Ratio_v_time_constant_array_size.png)

* I also wanted to look at how the initial number of inversions influenced the run time of selection sort. The first graph is with different tested array sizes while the second graph is with array size held constant at 10000.
![](Initial_num_inversions_diff_array_size.png)
![](Initial_inversions_v_time_constant_array_size.png)

* Another thing to look at was whether the number of initial inversions influenced how much sorting the program had to do. Below is the number of initial inversions versus the inversion ratio. Array size was held constant to account for this confounding variable.
![](Invers_v_ratio_constant_array_size.png)
 
