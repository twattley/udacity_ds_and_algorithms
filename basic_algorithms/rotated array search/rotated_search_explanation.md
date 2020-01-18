Design:

for the rotate array search a binary iterative search has been used, I intially started with 2 binary searches one to find the start of the list then one to split and find the index of the number before realising one iterative approach could solve the problem, recursive solutions were also considered but the iterative approach felt more natural 


time complexity: 

being binary search this is implemented in log(n) time every pass through the array cuts the search space in half so for an array of 8 only 3 passes are required

space complexity:

space complexity for the search is 0(n) the input space will grow in lionear proportion to the size of the memory allocated for the list, the auxiallry space used to continually cut the list in half will be 0(log n) therefore total complexity will O(n + logn)