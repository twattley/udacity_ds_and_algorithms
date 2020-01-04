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
    
    #create a joined array of both linked lists 
    duplicated_union = llist_1.to_list() + llist_2.to_list()
    
    non_duplicated = []
    for i in duplicated_union:
        if i not in non_duplicated:
            non_duplicated.append(i)
    return non_duplicated


def intersection(llist_1, llist_2):
    
    # convert both linked lists to arrays 
    list_1 = llist_1.to_list()
    list_2 = llist_2.to_list()
    
    intersection = []
    
    for i in list_1:
        if i in list_2:
            intersection.append(i)
            
    unique_intersection = []
    for i in intersection:
        if i not in unique_intersection:
            unique_intersection.append(i)
            
    return unique_intersection
            

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