import sys
import heapq
from collections import Counter
import unittest

class HuffmanTree:
    
    """the function of this class is to build the huffman tree instantiated with a string"""
    
    def __init__(self, input_string):
        self.input_string = input_string
    
    @staticmethod
    def traverse_tree(tree, mapper, prefix):
        
        """ recursively traverse tree """
        
        if len(tree) == 1:
            frequency, label = tree[0]
            mapper[label] = prefix
        else:
            value, left, right = tree
            HuffmanTree.traverse_tree(left, mapper, prefix + '0') #walk tree to the left add 1
            HuffmanTree.traverse_tree(right, mapper, prefix + '1') #walk tree to the right add 0
    

    def print_sizes(self):
        
        print (f"The size of the data is: {sys.getsizeof(self.input_string)}\n")
        print (f"The content of the data is: {self.input_string}\n")

        print (f"The size of the encoded data is:{sys.getsizeof(int(self.encode(), base=2))}\n")
        print (f"The content of the encoded data is: {self.encode()}\n")

        print (f"The size of the decoded data is: {sys.getsizeof(self.decode())}\n")
        print (f"The content of the encoded data is: {self.decode()}\n")
   
        
    def huffman_frequency_counter(self):
        
        """ create a frequency dictionary """

        if not self.input_string:
            raise ValueError('Invalid input string must be instantiated with string of characters')
        
        if not type(self.input_string) == str:
            raise TypeError('Huffman Coder only works with string input')

        frequency_dict = Counter()
        for letter in self.input_string:
            frequency_dict[letter] += 1
            
        total = sum(frequency_dict.values())
        
        frequency_dict = {i:v/total for i, v in frequency_dict.items()} #normalise frequency values
        
        return [(v,i) for i,v in frequency_dict.items()]

    
    def build_tree(self):
        
        """ build huffman tree """
        
        #create frequencies of input
        frequencies = self.huffman_frequency_counter()
        
        huffman_heap = []
        
        for letter in frequencies:
            heapq.heappush(huffman_heap, [letter])
        
        while len(huffman_heap) > 1:
            
            #using lowest values heap property push new values on 
            left_child = heapq.heappop(huffman_heap)
            right_child = heapq.heappop(huffman_heap)
            
            frequency_left, label_left = left_child[0]
            frequency_right, label_right = right_child[0]
            frequency = frequency_left + frequency_right
            
            label = ''.join(sorted(label_left + label_right))
            huffman_node = [(frequency, label), left_child, right_child]
            heapq.heappush(huffman_heap, huffman_node)
    
        return huffman_heap.pop()
    
            
    def build_code_mappings(self):
        
        """ walk through huffman tree adding prefix'/labels"""
        
        codemap = {}
        
        #build code tree
        tree = self.build_tree()
        HuffmanTree.traverse_tree(tree, codemap, '')
        
        return codemap
        
        
    
    def encode(self):
        
        """ loop through the dictionary and add them to a list """
        
        mappings = self.build_code_mappings()
        encoded = ''.join([mappings[letter] for letter in self.input_string])
    
        return encoded
        
        
    def decode(self):
        
        """decode the string back into original """
        
        tree = self.build_tree()
        traverser = self.build_tree()
        
        encoded_message = self.encode()
        
        decoded_letters = []
        for digit in encoded_message:
            if digit == '0': 
                traverser = traverser[1]
            else: 
                traverser = traverser[2]
           
            if len(traverser) == 1:   #check if at leaf/bottom of tree
                _ , label = traverser[0]
                decoded_letters.append(label)
                traverser = tree
            
        decoded_string = ''.join(decoded_letters)
        
        return decoded_string
        
    

class TestStringMethods(unittest.TestCase):
    
    """ test cases for huffman encoder """

    def test_int_error(self):
        with self.assertRaises(TypeError):
            HuffmanTree(45).encode()
    
    def test_empty_str_error(self):
        with self.assertRaises(ValueError):
            HuffmanTree('').encode()
    
    def test_correct_input(self):
        input_str = 'aaaccccbcbabdaba'
        huffman = HuffmanTree(input_str)
        self.assertTrue(huffman.encode() == '0001111111110111101010110001010')
        self.assertTrue(huffman.build_code_mappings() == {'a': '0', 'd': '100', 'b': '101', 'c': '11'})
        self.assertTrue(huffman.decode() == input_str)
        
#run tests
unittest.main(argv=['first-arg-is-ignored'], exit=False)