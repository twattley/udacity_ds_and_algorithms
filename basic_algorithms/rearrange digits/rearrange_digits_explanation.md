Design:

the general design of the problem is to notice that the greatest sum can be found by sorting a list and then alternately taking from the list splitting into 2. as the algorithm was required to run in 0(n log n) I had options of heapsort or merge sort.

A reverse merge sort was implemented and a helper using the invariant that splitting the list by indexes divisble by 2 nicely takes every other element from one list and the inverse takes the other inclusive

time complexity:

the reverse merge sort function runs on 0(n*log n) the first n being the number of splits to be made, the log n representing the binary element of comparing the numbers.

The helper function is order 0(n) linear time in that it must run through a list and split into to thus making the whole algorithm run in (n*log n + n) the dominant term here n*logn


space complexity:

space for this algorithm 0(3n) which simplifies to 0(n) where n is the length of the list 

first of there is the call stack in the recursive merge this is 0(n) linearly growing with input size, there are 2 other space considerations, the merged auxillary list in the reverse merge function and returned list within the rearrange digits function