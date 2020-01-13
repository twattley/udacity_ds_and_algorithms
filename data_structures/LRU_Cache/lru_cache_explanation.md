
## Design:
the lru cache has been implemented via a combination of a hash map and a linked list the key being that given and the value being a node with previous and next attributes, these structures have been chosen to for optimal get and set methods in the class

## Time Complexity
* set_val:
set val runs in 0(1) constant time this is done by simply adding a node and adjusting the pointers accordingly 

* get:
get uses a python dictionary to lookup the node and again is therefore a 0(1) constant time operation

## Space Complexity
space is a linear concern 0(n) as it will grow depending on the size of the cache specified