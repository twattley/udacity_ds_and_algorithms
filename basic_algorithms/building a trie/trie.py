import unittest

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
    
    def insert(self, letter):
        ## Add a child node in this Trie
        if letter not in self.children:
            self.children[letter] = TrieNode()
            
    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        words = []
        for letter, child in self.children.items():
            if child.is_word:
                words.append(suffix+letter)
            words += child.suffixes(suffix+letter)
        return words


class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        trie_node = self.root #head node
        for letter in word:   
            trie_node.insert(letter)   #add letter create children dict
            trie_node = trie_node.children[letter] #
        trie_node.is_word = True
            

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        if prefix not in trie_node.children:
            return False
        trie_node = self.root
        for letter in prefix:
            trie_node = trie_node.children[letter]
        return trie_node



