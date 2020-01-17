Design:

the template for the http trie router was designed by Udacity, it contains a trie node inside a trie inside a router wrapper class. The trie node is a hashmap with a handler that is assigned by the trie to the end of a http when added to the trie.

The routetrie has insert and find methods, these walk through parts of the path and insert trie nodes this time words rather than letters and the find function is a traversal/Sophisticated nested dictionary lookup. These functionalitys are wrapped up in a Router class

Time Complexity:

the time complexity for creating a trie is O(n * p) where n is the number of words and p is the number of parts to the http link, the hashmap lookups are in constant time 0(1) so O(n * p) is the dominant term

Space Complexity:

the space complexity is a little different from the basic trie as full words are being put in (n * p) where n is the number of entries and p is the number of parts to the http link

the stack isnt used to search in this router