## Design:
the blockchain has been implemented as a linked list, it has been chosen as the need to linked each part to the previous to form a chain via hashes is necessary and the ability to prepend in constant time with the size unknown makes this more suitable than a contiguous block of memory

## Time Complexity
* Appending:
blocks are appended to the chain in 0(1) constant time this is done by simply pointing the last block at the new one 

* Traversing:
a block will be searched with 0(n) complexity in worst case scenario

## Space Complexity
* Size:
O(n) the size of the blockchain in memory will grow at a constant rate in direct linear size with the input