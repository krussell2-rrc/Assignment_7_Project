import unittest
from unittest import TestCase
from input_handler.input_handler import InputHandler
from unittest.mock import patch, mock_open
import csv
class InputHandlerTests(TestCase):
    
    # get_file_format tests
    
    def test_get_file_format_csv(self):
        # Arrange
        file_path = "test.csv"
        target = InputHandler(file_path= file_path)

        # Act
        actual = target.get_file_format()

        # Assert
        expected = "csv"
        self.assertEqual(expected, actual)    

    def test_get_file_format_json(self):
        # Arrange
        file_path = "test.json"
        target = InputHandler(file_path= file_path)

        # Act
        actual = target.get_file_format()

        # Assert
        expected = "json"
        self.assertEqual(expected, actual)  

    def test_get_file_format_empty(self):
        # Arrange
        file_path = "test."
        target = InputHandler(file_path= file_path)

        # Act
        actual = target.get_file_format()

        # Assert
        expected = ""
        self.assertEqual(expected, actual)  
    
    # read_csv_data tests

    def test_read_csv_data_populated(self):
        # Arrange
        file_contents = (
            "Transaction ID,Account number,Date,Transaction type,Amount,Currency,Description\n"
            "1,1001,2023-03-01,deposit,1000,CAD,Salary\n"
        )
        filename = "test.csv"

        expected_output = [
        {'Transaction ID': '1', 'Account number': '1001', 'Date': '2023-03-01', 'Transaction type': 'deposit', 'Amount': '1000', 'Currency': 'CAD', 'Description': 'Salary'}]

        # Act
        with patch('builtins.open', mock_open(read_data=file_contents)):
            handler = InputHandler(filename)
            actual_output = handler.read_csv_data()

        # Assert
        self.assertEqual(actual_output, expected_output)

    def test_read_csv_data_empty(self):
        # Arrange
        file_contents = ""
        
        filename = "test.csv"

        expected_output = []

        # Act
        with patch('builtins.open', mock_open(read_data=file_contents)):
            handler = InputHandler(filename)
            actual_output = handler.read_csv_data()

        # Assert
        self.assertEqual(actual_output, expected_output)

    def test_read_csv_data_exception(self):
        # Arrange
        file_contents = (
            "Transaction ID,Account number,Date,Transaction type,Amount,Currency,Description\n"
            "1,1001,2023-03-01,deposit,1000,CAD,Salary\n"
        )
        filename = "doesnotexist.csv"

        target = InputHandler(file_path= filename)

        # Act
        with self.assertRaises(FileNotFoundError) as context:
            target.read_csv_data()

        # Assert
        self.assertEqual(str(context.exception), "File: doesnotexist.csv does not exist.")

    def test_read_input_data(self):
        # Arrange
        file_contents = (
            "Transaction ID,Account number,Date,Transaction type,Amount,Currency,Description\n"
            "1,1001,2023-03-01,deposit,1000,CAD,Salary\n"
        )
        filename = "test.csv"

        expected_output = [
        {'Transaction ID': '1', 'Account number': '1001', 'Date': '2023-03-01', 'Transaction type': 'deposit', 'Amount': '1000', 'Currency': 'CAD', 'Description': 'Salary'}]

        # Act
        with patch('builtins.open', mock_open(read_data=file_contents)):
            handler = InputHandler(filename)
            actual_output = handler.read_input_data()

        # Assert
        self.assertEqual(actual_output, expected_output)

    def test_read_input_data_empty(self):
        # Arrange
        file_contents = "Transaction ID,Account number,Date,Transaction type,Amount,Currency,Description\n1,1001,2023-03-01,deposit,1000,CAD,Salary\n"
        
        filename = "test.gif"

        expected_output = []

        # Act
        with patch('builtins.open', mock_open(read_data=file_contents)):
            handler = InputHandler(filename)
            actual_output = handler.read_input_data()

        # Assert
        self.assertEqual(actual_output, expected_output)

if __name__ == "__main__":
    unittest.main()