import hashlib
import time

class Block:

    def __init__(self, data, previous_hash = None):
        self.timestamp = self.calc_timestamp()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(data)
    
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
    
    def __init__(self, head=None):
        self.head = head
        self.size = 0
        
        
    def prepend(self, value):
        
        """ add values to the blockchain """
        
        if not self.head:
            self.head = Block(value)
            self.size +=1
        else:
            self.head = Block(value, self.head)
            self.size +=1
            
    def return_size(self):

        """ return the size of the blockchain """

        return self.size
    
    def to_dict(self):
        
        """ create a dictionary of the blockchain for viewing """
        
        out = {}
        block = self.head
        while block:
            out[block.data] = {
                'Block':block,
                'TimeStamp':block.timestamp,
                'Hash':block.hash,
                'Previous Block':block.previous_hash}
            block = block.previous_hash
        return out