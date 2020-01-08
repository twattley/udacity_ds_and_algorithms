import unittest

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size
    
    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out




def union(llist_1, llist_2):
    
    if not llist_1:
        raise ValueError ('list 1 empty, must contain a value')
    
    if not llist_2:
        raise ValueError ('list 2 empty, must contain a value')
        
    list_1 = llist_1.to_list()
    list_2 = llist_2.to_list()
    
    non_duplicated = set(list_1 + list_2)
    
    union_linked_list = LinkedList()
    
    for item in non_duplicated:
        union_linked_list.append(item)

    return union_linked_list


def intersection(llist_1, llist_2):
    
    if not llist_1:
        raise ValueError ('list 1 empty, must contain a value')
    
    if not llist_2:
        raise ValueError ('list 2 empty, must contain a value')
        
    # convert both linked lists to arrays 
    set_1 = set(llist_1.to_list())
    set_2 = set(llist_2.to_list())

    intersection = LinkedList()
    
    for i in set_1:
        if i in set_2:
            intersection.append(i)
            
    return intersection
            

def create_linked_lists(list_1, list_2):
    
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = list_1
    element_2 = list_2

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)
        
    return linked_list_1, linked_list_2


def test_union(llist_1, llist_2):
    
    """function using built ins to test union function """
    
    return list(set(llist_1.to_list() + llist_2.to_list()))


def test_intersection(llist_1, llist_2):
    
    """function using built ins to test intersection function """
    
    return list(set(llist_1.to_list()).intersection(set(llist_2.to_list())))


def test_union_and_intersection():

    """ function to test the intersection and union functions """
    
    x = [3,2,4,35,6,65,6,4,3,21]
    y = [6,32,4,9,6,1,11,21,1]
    llist_1, llist_2 = create_linked_lists(x, y)
    
    assert sorted(test_union(llist_1, llist_2)) == sorted(union(llist_1, llist_2))
    assert sorted(test_intersection(llist_1, llist_2)) == sorted(intersection(llist_1, llist_2))
    
    x = [3,2,4,35,6,65,6,4,3,23]
    y = [1,7,8,9,11,21,1]
    llist_1, llist_2 = create_linked_lists(x, y)
    
    assert sorted(test_union(llist_1, llist_2)) == sorted(union(llist_1, llist_2))
    assert sorted(test_intersection(llist_1, llist_2)) == sorted(intersection(llist_1, llist_2))
    
    
    x = [1,1,2,3,4,4,5,6,7,8,9,10]
    y = [1,2,3,4,5,6]
    llist_1, llist_2 = create_linked_lists(x, y)
    
    assert sorted(test_union(llist_1, llist_2)) == sorted(union(llist_1, llist_2))
    assert sorted(test_intersection(llist_1, llist_2)) == sorted(intersection(llist_1, llist_2))
    
test_union_and_intersection()   

class TestUnionIntersection(unittest.TestCase):
    
    """ test edge cases raise error """
    

    def test_input_error_1(self):
        with self.assertRaises(ValueError):
            union('',[1,2,3,4])
    
    def test_input_error_2(self):
        with self.assertRaises(ValueError):
            intersection('',[1,2,3,4])
    
#run tests
unittest.main(argv=['first-arg-is-ignored'], exit=False)