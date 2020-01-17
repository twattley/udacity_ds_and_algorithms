class RouteTrieNode:
    
    def __init__(self, handler=None):
        self.children = {}
        self.handler = handler
    
    def insert(self, path_part):
        if path_part not in self.children:
            self.children[path_part] = RouteTrieNode
            
class RouteTrie:
    
    def __init__(self, handler):
        self.root = RouteTrieNode(handler)
        
    def insert(self, path_parts, handler):
        
        """ insert parts of the path into nested trie nodes """
        
        route_trie_node = self.root
        for part in path_parts:
            route_trie_node.children[part] = RouteTrieNode() #instantiate node 
            route_trie_node = route_trie_node.children[part] #move root node along
        route_trie_node.handler = handler                    #assign state at leaf    
            
    
    def find(self, path_parts):
        
        """ given path parts find the handler """
        
        route_trie_node = self.root
        for part in path_parts:
            if not part in route_trie_node.children: return None
            else:
                route_trie_node = route_trie_node.children[part]
        return route_trie_node.handler


class Router:
    
    """ wrapper class around RouteTrie class 
    
    implements adding handler and lookup functions
    
    
    """
    
    def __init__(self, handler=None, not_found=None):
        
        self.router = RouteTrie(handler)
        self.not_found = not_found

    def add_handler(self, path, handler):
        
        path_parts = self.split_path(path)
        self.router.insert(path_parts, handler)
 
    def lookup(self, path):
        
        path_parts = self.split_path(path)
        handler = self.router.find(path_parts)
        
        if not handler:
            return self.not_found
        
        return handler
    
    def split_path(self, path): 
        return [item for item in path.split("/") if item]  #split and filter emptys
  
    
        

# create the router and add a route
ROUTER = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this

handlers = [
    
    '/some/random/handler',
    '/another/random/handler/with/a/trailing/',
    '/oh/look/heres/another/one/',  
]

for i in handlers:
    ROUTER.add_handler(i, "test handler")  # add a route

def test_route_trie_handler_function():
    
    """ small test function to test the router is working correctly """
    
    assert ROUTER.lookup('/some/random/handler') == 'test handler'
    assert ROUTER.lookup('/another/random/handler/with/a/trailing/') == 'test handler'
    assert ROUTER.lookup('/oh/look/heres/another/one/') == 'test handler'
    assert ROUTER.lookup('/some/random/handler/that/should/fail') ==  "not found handler"
    assert ROUTER.lookup('/oh/look/heres/another/one/that/should/fail') ==  "not found handler"


test_route_trie_handler_function()