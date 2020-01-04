there are quite a few parts to the huffman encoding implementation class

- initial frequency counter - I lent on pythons optimised collections counter there are a few linear loops within this functions, one loop through the input string, one to sum the values, one normalise and one to return a list of tuples, this function has a time complexity of 0(n)

- build tree - all the letters are pushed onto the tree, 0(n), the heapq library has done most of the heavy lifting in this function a tree is built as an array/python list, values are pushed onto the heap lowest 2 popped off and joined in a node this is again done in linear time 

- build code mappings - this is done using a recursive tree walking helper function and a hashing function in linear time

- encode - values are joined in a string in linear time 

- decode - this is done using iteration however potnetially this maybe could have been done recursively th tree is simply walked checking if it is a leaf node and getting the label else moving down the tree, letters are then jined into a string all operations done in linear time 


the space complexity of the huffman tree is proportional to input and the worst time complexity out of the helpers is also linear