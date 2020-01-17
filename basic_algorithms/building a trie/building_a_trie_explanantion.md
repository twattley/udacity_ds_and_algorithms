Design:

The design for building a trie was templated by Udacity

there are 2 parts to building the trie, nodes initially are little more than stateful dictionaries and the tree that the nodes form which are at their core sophisticated dictionary lookups

Time Complexity:

for the node there are 2 operations insert and suffixes, insert will be done in constant time it is one letter hashed into a dictionary, the suffix function finds the first letter of the word which has a max input of 26, the complexity of this function depends on how many words are in there so it is O(n * lw) where n is the number of words and lw is the length of the words

Insert for the Trie itself will be O(n) as it must go through the word letter at a time and create/hash new trie nodes so it will be linearly correlated with the input space ie the word its given. Find is also linear O(n) for the same reasons as insert it is proportional to input size. 


Space Complexity:

the space complexity is a little more complicated there is the space taken by insert which is are nested dictionarys the use of tries will save space when words have some of the same letters but purely in a worst case scenario the space will roughly speaking be 0(n * m) where n is the number of entries and m is the length of the words

the stack is used as auxillary space when recursing through suffixes to find the word and will be O(n * log a) where n is the number of words input and a in this case is the 26 letters of the alphabet as letters are typed the predictive algorithm will continue to cut by a combinatorial factor proportional to the letters in the alphabet  