import unittest
from unittest.mock import mock_open, patch
from unittest import TestCase
from output_handler.output_handler import OutputHandler


class TestOutputHandler(TestCase):
    """The following constants have been provided to reduce the amount of 
    code needed when creating OutputHandler class objects in the tests that 
    follow.  To use the constants, prefix them with self.  Examples:
    self.ACCOUNT_SUMMARIES
    self.SUSPICIOUS_TRANSACTIONS
    self.TRANSACTION_STATISTICS
    """

    ACCOUNT_SUMMARIES = { '1001': {'account_number': '1001', 'balance': 50, 
                            'total_deposits': 100, 'total_withdrawals': 50},
                            '1002': {'account_number': '2', 'balance': 200, 
                            'total_deposits': 200, 'total_withdrawals': 0}}
    
    SUSPICIOUS_TRANSACTIONS = [{"Transaction ID":"1" ,"Account number":"1001" ,
                            "Date":"2023-03-14" ,"Transaction type": "deposit",
                            "Amount":250,"Currency":"XRP","Description":"crypto investment"}  ]

    TRANSACTION_STATISTICS = {'deposit': {'total_amount': 300, 'transaction_count': 2}, 
                            'withdrawal': {'total_amount': 50, 'transaction_count': 1}}
        

    def test_write_account_summaries_to_csv(self):
        # Arrange
        with patch("builtins.open", mock_open()) as mock_file:
            file_name = "test_output.csv"
            file_contents = OutputHandler(self.ACCOUNT_SUMMARIES,[], {})

        # Act
            file_contents.write_account_summaries_to_csv(file_name)

        # Assert
            mock_file().write.assert_called()
            actual = mock_file().write.call_count
            expected = len(self.ACCOUNT_SUMMARIES) + 1 
            self.assertEqual(actual, expected)
        
    def test_write_suspicious_transactions_to_csv(self):
        # Arrange
        with patch("builtins.open", mock_open()) as mock_file:
            file_name = "test_output.csv"
            file_contents = OutputHandler(self.ACCOUNT_SUMMARIES, self.SUSPICIOUS_TRANSACTIONS, {})

        # Act 
            file_contents.write_suspicious_transactions_to_csv(file_name)

        # Assert
            mock_file().write.assert_called()
            actual = mock_file().write.call_count
            expected = len(self.SUSPICIOUS_TRANSACTIONS) + 1
            self.assertEqual(actual, expected)

    def test_write_transaction_statistics_to_csv(self):
        # Arrange
        with patch("builtins.open", mock_open()) as mock_file:
            file_contents = OutputHandler({}, [], self.TRANSACTION_STATISTICS)
            file_name = "test_output.csv"
            
        # Act
            file_contents.write_transaction_statistics_to_csv(file_name)

        # Assert
            mock_file().write.assert_called()
            actual = mock_file().write.call_count
            expected = len(self.TRANSACTION_STATISTICS) + 1
            self.assertEqual(actual, expected) 


if __name__ == "__main__":
    unittest.main()