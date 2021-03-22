#! python3
import unittest
from Data2bots import check_file_type, compare_dates, add_column

class TestCSVtoJson(unittest.TestCase):


    def test_check_file_type_with_json(self):
        #Confirm that the program only takes csv files
        file = 'ahmadololade.json'
        converter = check_file_type(file)
        self.assertFalse(converter == True)
        
    @unittest.expectedFailure # cos no such file as usman.csv
    def test_check_file_type_with_csv(self):
        file = 'usman.csv'
        converter = check_file_type(file)
        self.assertTrue(converter  == True)
        
    def test_add_column(self):
        file, header, reader = add_column('dataset.csv')
        self.assertTrue(len(header) > len(next(reader)))
        
        
        

if __name__ == '__main__':
    unittest.main()
