## Design:

the huffman coder is comprised of a few peices, the bulk of the work is done in the frequency counter and build tree functions, where heaps arrays and hashmaps are used as the data structures. the heap was chosen because it naturally places lower values down the tree and nested arrays nicely represent a tree structure, naturally a hash map was chosen to hold the mappings of letters to codes



## Time Complexity
* Encoding:
huffman frequency counter - 3 iterative loops + an interative sum loop over the input string mean this function is 0(n) linearly correlated with input size

build tree - heaps are linearithmic time O(n log n)

encode - is at its worst a recursive function using the helper walk tree to recurse over the structure to add 0's and 1's accordingly, this is a tree and therfore the time complexity O(2^n) which dominates and is the time complexity of the function

* Decoding:
the decode function builds trees and encodes the message which if considered in this case will cause the function to be O(2^n) dominated again by the heap tree building as the decoding itself will be in 0(n) linear time as it is a walk through the encoded message once while appending to an array

## Space Complexity
* Encoding:
the space complexity of the encoding is only O(n) as the recursive stack will only ever get as big as n

* Decoding:
the same is true for decode, the iterative loop through the tree is linearly correlated with the input