a hash map in the form of a python dictionary has been used as the data structure for the lru cache, some of the heavy lifting has been done by python since they introduced insertion order post 3.7 the most recently used/inserted item is at the tail of the dictionary,  thus meaning operations of get and set are done in constant time.

size is tracked by object state and I have simply unpacked the first element of the tuple and popped it out of the dictionary if it is full

space is a linear concern as it will grow depending on the size of the cache specified
