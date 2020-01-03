import os
import unittest

initial_folder = os.path.join(os.getcwd(), 'testdir')

def find_files(suffix, path):

    if not path:
        raise ValueError('no path specified')
    
    if not suffix:
        raise ValueError('no file suffix specified')
    
    if not type (suffix)  == str:
        raise TypeError('suffix must be input as string')
        
    if not type(path) == str:
        raise TypeError('filepath must be input as string')
    
    paths = []
    
    if os.path.isfile(path):
        if path.endswith(suffix):
            paths.append(path)

    if os.path.isdir(path):
        for child in os.listdir(path):
            child_path = os.path.join(path, child)
            paths.extend(find_files(suffix, child_path))


    return paths


class TestFileFunctions(unittest.TestCase):
    
    """ test cases for file recursion """

    def test_find_file_function(self):
        c_files = find_files('.c',initial_folder)
        for file in c_files:
            self.assertTrue (file.endswith('c'))
    

    def test_input_error(self):
        with self.assertRaises(TypeError):
            find_files(45,initial_folder)
    
    def test_empty_str_error(self):
        with self.assertRaises(ValueError):
            find_files('',initial_folder)
    


#run tests
unittest.main(argv=['first-arg-is-ignored'], exit=False)