import hashlib
import time
import unittest

class Block:

    def __init__(self, data, previous_hash = None):
        self.timestamp = self.calc_timestamp()
        self.data = data
        self.next = None
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(data) + self.timestamp
    
    def calc_hash(self, input_string):
    
        sha = hashlib.sha256()
        hash_str = input_string.encode('utf-8')
        sha.update(hash_str)

        return sha.hexdigest()
        
    def calc_timestamp(self):
        
        """ return string representation of gmt time """

        time_gmt = ''.join(str(i) for i in time.gmtime())
        return time_gmt
    

class BlockChain:
    
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.previous_hash_data = None
        self.size = 0
        
    def append(self, data):
        
        #check foir valid input
        if not data:
                raise ValueError('must input data into the blockchain')
        #empty blockchain case
        if self.head is None:
            #force data to string
            data = str(data)
            self.head = Block(data)
            self.tail = self.head
            self.previous_hash_data = self.head.hash
            self.size += 1
            return
        else:
            #force data to string
            data = str(data)
            new_block = Block(data)  
            new_block.previous_hash = self.previous_hash_data
            self.previous_hash_data = new_block.hash
            new_block.next = self.head
            self.head = new_block
            self.size += 1
        return
        
            
    def return_size(self):

        """ return the size of the blockchain """

        return self.size
    
    def data_to_list(self):
        
        out = []
        block = self.head
        while block:
            out.append(block.data)
            block = block.next
        
        return out 
        
    
    def to_dict(self):
        
        """ create a dictionary of the blockchain for viewing """
        
        out = {}
        block = self.head
        while block:
            
            out[block.data] = {
                'TimeStamp':block.timestamp,
                'Hash':block.hash,
                'Previous Block Hash':block.previous_hash}
            block = block.next
        return out

    
    
#Instantiate the blockchain and append for testing 
test_blockchain = BlockChain()
block_test_range = ['a','b','c','d']
for i in block_test_range:
    test_blockchain.append(i)
    
#create dictionary for testing
test_blockchain_dict = test_blockchain.to_dict()




class TestBlockChain(unittest.TestCase):
    
    """ test blockchain suite """
    
    def test_previous_hashing(self):
        
        """ assert hashing function works correctly """
        
        assert (test_blockchain_dict['a']['Hash']) == \
        (test_blockchain_dict['b']['Previous Block Hash'])
        assert (test_blockchain_dict['b']['Hash']) == \
        (test_blockchain_dict['c']['Previous Block Hash'])
        assert (test_blockchain_dict['c']['Hash']) == \
        (test_blockchain_dict['d']['Previous Block Hash'])
        
    def test_input_error(self):
        #chain should raise value error when no input 
        with self.assertRaises(ValueError):
            test_blockchain.append('') 
    
    def test_int_input(self):
        #shouldnt throw error
        test_blockchain.append(5)
    
#run tests
unittest.main(argv=['first-arg-is-ignored'], exit=False)