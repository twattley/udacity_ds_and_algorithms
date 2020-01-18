Design:

the implementation of the sorting012 algorithm is done by using the index pointers in an array, originally 3 variables are set, 
- one where the last 0 is found this is set to 0, 
- one where the first 2 is found this is originally set to the last index in the list 
- an iterating pointer to be incremented in the while loop

when traversing the list if a 0 or 2 is found that a reverse operation is performed, the 0 or 2 being inserted wherever their variable indexes are pointing to and the index nudged up for 0's down for 2's one is the pivot in 012 and is left alone

Time complexity:

one traversal of the list values are changed in place so to sort linear time 0(n) 

Space complexity:

space complexity id the size of the list + 3 index variables so this is list 0(n) + 3 variables 0(1) the linear part od this dominating giving overall space complexity of O(n) growing linearly with size of input in the worst case