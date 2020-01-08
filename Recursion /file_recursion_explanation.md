## Design:
A recursive algorithm is used for the file search as the input is unknown and a recursive structure will be suitable as this problem although about files is identical to tree traversal and it will simply traverse all parts of the tree


## Time Complexity
in terms of time complexity the time taken to excute depends on the number of directories so can be described as 0(sd * n) where sd equals sub directories

## Space Complexity
an output empty list is designated to hold all recurrences and in the worst case could hold all the folders/subfolders
the call stack for the function will also be where space gets taken up as frames are added until the condition or base case is met and this is not known beforehand this will be 0(n) 