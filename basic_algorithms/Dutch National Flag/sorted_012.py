import unittest

def sort_012(input_list):
    
    if not input_list:
        raise ValueError('no list input!!')
    
    last_0 = 0                   #pointer to last 0 index
    first_2 = len(input_list)- 1 #pointer to first 2 index
    index = 0                    #index counter 
    
    while index <= first_2:
        
        if not isinstance(input_list[index], int):
            raise TypeError('values must be of type integer')

        #case where index is 0
        if input_list[index] == 0:
            input_list[index] = input_list[last_0] #reverse positions
            input_list[last_0] = 0 
            last_0 += 1
            index += 1
            
        #case where index is 2    
        elif input_list[index] == 2:
            input_list[index] = input_list[first_2] #reverse positions
            input_list[first_2] = 2
            first_2 -= 1
            
        #case where index is 1 leave 
        elif input_list[index] == 1:
            index += 1 
            
        else:
            raise ValueError('sort_012 requires 0/1/2 values input')
    
    return input_list
        
#generate some dummy test data
LIST_A = [2, 2, 0, 1, 1, 0, 0, 2, 2, 2, 1, 1, 2, 2, 2, 1, 1, 1, 0, 0]
LIST_B = [0, 1, 2, 1, 0, 0, 2, 2, 1, 1, 1, 1, 2, 2, 0, 0, 2, 2, 0, 0]
LIST_C = [2, 0, 2, 2, 1, 1, 1, 2, 1, 0, 2, 2, 1, 1, 1, 0, 0, 0, 2, 2]

class TestSort012(unittest.TestCase):
    
    """ test sort 012 function """

    def test_no_input_error(self):
        with self.assertRaises(ValueError):
            sort_012('')
    
    def test_typeError(self):
        with self.assertRaises(TypeError):
            sort_012([1,2,'some_string',0])
            
    def test_valueError(self):
        with self.assertRaises(ValueError):
            sort_012([1,2,3,0])
            
    def test_correct_input(self):
        assert sort_012(LIST_A) == sorted(LIST_A)
        assert sort_012(LIST_B) == sorted(LIST_B)
        assert sort_012(LIST_C) == sorted(LIST_C)
    
#run tests
unittest.main(argv=['first-arg-is-ignored'], exit=False)