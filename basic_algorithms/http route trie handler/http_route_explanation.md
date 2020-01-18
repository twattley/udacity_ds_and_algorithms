Design:

the template for the http trie router was designed by Udacity, it contains a trie node inside a trie inside a router wrapper class. The trie node is a hashmap with a handler that is assigned by the trie to the end of a http when added to the trie.

### Design:

there are 3 parts to the http route trie handler 

a route trie node - these are the building blocks for the trie each containing a hash map relating to the nested subfolders contained within them, they alse have a state variable handler which denotes whether this node is a handle, the trie sets this variable in its insert function when it hits a leaf node

the route trie - this is the trie structure part, it has an insert and find function, insert starts at the root node takes a list of words and nests each part as a node inside another node finally setting the last node to the handler input value, find is similar in structure in that it starts at the root traverses the nodes and returns the handler

the Router - the router wraps the trie and the trie nodes into one class, the add handler function uses the helper to split the path by '/' insert can then iteratively nest the list structure into the trie setting the handler, the lookup again uses the split path helper function and the fins function to iteratively look inside the nested tries for that part of the path. the split path helper uses a pythions string splitting inside a list comprehension to gather the parts after splitting the if item acts as a filter for whitespace




### Time Complexity:
* insert:
to split the address up we have a complexity of 0(n) it will have to scan the string, insert then traverses a list comprised of the number of words in the address hashing them in constant time, the initial search through all the letters will always be larger than iterating through the list and hashing, therefore the upper bound on this is 0(n) linear with the size of input

* find:
find again uses the split function same as insert 0(n), time complexity comments as in the insert apply here

### Space Complexity:
* insert 
initially to insert you split the address into parts, this is one array of auxillary space and size will vary linearly with input O(n), then these are hashed one by one this again will be O(n) the number of nested dictionarys linearly correlating with input, the variable handler is constant 0(1) it will always be the same size ignoring length of string

* find (*hint: you are splitting the path string to a list, then using this to find the handler):
the find function only needs the list split into parts for the algorithm giving an 0(n) linear complexity