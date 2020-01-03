class LRU_Cache(object):

    def __init__(self, capacity):
        self.hash_map = {}
        self.capacity = capacity
        self.size = 0
        self.is_empty = True
        self.hash_map.keys()

    def get(self, key):
        
        #get value
        #pop item from dict
        #re-add item to front 
        try:
            value = self.hash_map[key]
            self.pop_used_item(key)
            self.set_val(key, value)
            return value
        except KeyError:
            return -1

    def set_val(self, key, value):
        
        if self.cache_full():
            self.pop_last_item()
        
        self.hash_map[key] = value
        self.size += 1
    
    def cache_full(self):
        if self.size == 5:
            return True
        return False
    
    def pop_last_item(self):
        key_list = tuple(self.hash_map.keys())
        lru_key, *keys = key_list
        self.hash_map.pop(lru_key)
        self.size -= 1

    
    def pop_used_item(self, key):
        self.hash_map.pop(key)
        self.size -= 1

        
    def cache_to_list(self):
        return list(self.hash_map.items())



def test_lru_cache():
    
    test_range = [1,2,3,4,5]
    test_cache = LRU_Cache(5)
    
    #fill cache with range
    for index, value in enumerate(test_range):
        test_cache.set_val(index+1, value)
        
    #retrieve first item
    assert test_cache.get(3) == 3
    
    #look for missing item
    assert test_cache.get(6) == -1
    assert test_cache.cache_full()
    
    
    test_cache.set_val(6, 6)
    assert test_cache.size == 5
    
    #check most recent is the 6 just added
    assert test_cache.cache_to_list()[-1] == (6, 6)
    
    #check 2nd to most recent is the 3 previously retrieved/used
    assert test_cache.cache_to_list()[-2] == (3, 3)
    
    test_cache.set_val(7, 7)
    test_cache.set_val(8, 8)
    test_cache.set_val(9, 9)
    test_cache.set_val(1, 1)
    test_cache.get(7)
    #check most recent is the 7 just fetched
    assert test_cache.cache_to_list()[-1] == (7, 7)
    
    #check 3 is no longer in the cache and returns -1
    assert test_cache.get(3) == -1
    
    
    
test_lru_cache()    