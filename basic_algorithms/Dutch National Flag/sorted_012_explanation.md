Design:

I had originally considered using a dictionary or class to keep track of insertion states however the sort 012 has been implemented by instantiating 3 lists and appending to the correct list, the lists then simply need concatenating together into one in the correct order

Time complexity:

one traversal of the list to sort so linear time 0(n) having to go through every item and then 2 list concatenations in constant time 0(1) giving an overall time complexity of 0(n)

Space complexity:

for space there is the original list input size which is 0(n) and there is auxillary space for the 3 input lists but they are guarranteed not to grow any larger than the input list so again 0(n)