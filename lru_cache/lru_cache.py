import unittest

class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class LRU_Cache(object):

    def __init__(self, capacity):
        self.cache = {}
        self.capacity = capacity
        self.size = 0
        self.head = None
        self.tail = None
        
    def set_val(self, key, value):
        
        if not key:
            raise KeyError ('Key must be a valid entry')
        
        if not value:
            raise ValueError ('Value added to cache must be a valid entry')
        
        #remove last item if full
        if self.cache_full():
            self.pop_last_item()
        
        #empty cache
        if self.size == 0:
            self.head = DoubleNode(value)
            self.cache[key] = self.head
            self.tail = key
            self.size += 1 #update state
        else:
            new_cache_node = DoubleNode(value) #create new node
            new_cache_node.next = self.head.value
            self.head.previous = new_cache_node.value
            self.head = new_cache_node
            self.cache[key] = self.head
            self.size += 1 #update state
    
    
    def pop_last_item(self):
        
        lru_item = self.tail
        self.tail = self.cache[lru_item].previous
        self.cache[self.tail].next = None 
        self.cache.pop(lru_item)
        self.size -= 1
        
    def pop_used_item(self, key):
        
        """ remove an item to be replaced at the front of cache """
    
        #deal with pointers and pop from dictionary
        previous_pointer = self.cache[key].previous 
        next_pointer = self.cache[key].next 
       
        #deal with the end of the list case
        if not next_pointer:
            self.cache[previous_pointer].next = next_pointer
            self.size -= 1
        #deal with the start of the list case
        elif not previous_pointer:
            self.cache[next_pointer].previous = previous_pointer
            self.size -= 1
        #else correct pointers
        else:
            self.cache[previous_pointer].next = next_pointer
            self.cache[next_pointer].previous = previous_pointer
            self.size -= 1
        #pop from dictionary 
        self.cache.pop(key)
    
    
    def get(self, key):
        
        try:
            #store return value in a variable
            return_value = self.cache[key].value
            #remove and re set 
            self.pop_used_item(key)
            self.set_val(key, return_value)

            return return_value
        
        except KeyError:
            
            return -1
    
    def cache_full(self):
        
        """ boolean indicating if cache is full """
        
        if self.size == self.capacity:
            return True
        return False
        
    def return_cache(self):
        
        """ debugging function """
        
        return {key:value.value for key,value in self.cache.items()}
    

TEST_RANGE = [1,2,3,4,5]
TEST_CACHE = LRU_Cache(5)

#fill cache with range
for index, value in enumerate(TEST_RANGE):
    TEST_CACHE.set_val(index+1, value)

def test_lru_cache():
    
    """ standard cases for testing the lru cache """
        
    #retrieve first item
    assert TEST_CACHE.get(3) == 3
    
    #look for missing item
    assert TEST_CACHE.get(6) == -1
    assert TEST_CACHE.cache_full()
    
    
    TEST_CACHE.set_val(6, 6)
    assert TEST_CACHE.size == 5
    
    #check most recent is the 6 just added
    assert list(TEST_CACHE.return_cache().keys())[-1] == 6
    
    #check 2nd to most recent is the 3 previously retrieved/used
    assert list(TEST_CACHE.return_cache().keys())[-2] == 3
    
    TEST_CACHE.set_val(7, 7)
    TEST_CACHE.set_val(8, 8)
    TEST_CACHE.set_val(9, 9)
    TEST_CACHE.set_val(1, 1)
    TEST_CACHE.get(7)
    #check most recent is the 7 just fetched
    assert list(TEST_CACHE.return_cache().keys())[-1] == 7
    
    #check 3 is no longer in the cache and returns -1
    assert TEST_CACHE.get(3) == -1
    
    
test_lru_cache()

class TestLRUEdgeCases(unittest.TestCase):
    
    """ test edge cases for lru cache """
    

    def test_key_error(self):
        with self.assertRaises(KeyError):
            TEST_CACHE.set_val('', 6)
    
    def test_value_error(self):
        with self.assertRaises(ValueError):
            TEST_CACHE.set_val(6, '')
    
#run tests
unittest.main(argv=['first-arg-is-ignored'], exit=False)