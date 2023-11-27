import unittest
from unittest import TestCase
from data_processor.data_processor import DataProcessor

class TestDataProcessor(TestCase):
    """The following constant has been provided to reduce the amount of 
    code needed when creating DataProcessor class objects in the tests that 
    follow.  To use the constant, prefix it with self.  Examples:
    self.INPUT_DATA
    e.g.:  data_procesor = DataProcessor(self.INPUT_DATA)
    """
    INPUT_DATA = [{"Transaction ID":"1" ,"Account number":"1001" ,
                "Date":"2023-03-01" ,"Transaction type": "deposit",
                "Amount":1000,"Currency":"CAD","Description":"Salary"}, 
                {"Transaction ID":"2" ,"Account number":"1002" ,
                "Date":"2023-03-01" ,"Transaction type": "deposit",
                "Amount":1500,"Currency":"CAD","Description":"Salary"}]

    def setUp(self):
        self.data_processor = DataProcessor(self.INPUT_DATA)

    def test_update_account_summary_deposit(self):
        # Arrange
        deposit_data = self.INPUT_DATA[0]

        # Act
        self.data_processor.update_account_summary(deposit_data)
        account_summary = self.data_processor._account_summaries["1001"]

        # Assert
        self.assertEqual(account_summary["balance"], 1000)
        self.assertEqual(account_summary["total_deposits"], 1000)
        self.assertEqual(account_summary["total_withdrawals"], 0)


    def test_update_account_summary_withdrawal(self):
        # Arrange
        deposit_data = self.INPUT_DATA[0]
        withdrawal_data = {"Transaction ID": "3", "Account number": "1001", "Date": "2023-03-02",
                           "Transaction type": "withdrawal", "Amount": 500, "Currency": "CAD",
                           "Description": "Groceries"}
        
        # Act
        self.data_processor.update_account_summary(deposit_data)
        self.data_processor.update_account_summary(withdrawal_data)
        account_summary = self.data_processor._account_summaries["1001"]

        # Assert
        self.assertEqual(account_summary["balance"], 500)
        self.assertEqual(account_summary["total_deposits"], 1000)
        self.assertEqual(account_summary["total_withdrawals"], 500)


    def test_check_suspicious_transactions_large(self):
        # Arrange
        large_amount = {"Transaction ID": "3", "Account number": "1001", "Date": "2023-03-02",
                             "Transaction type": "withdrawal", "Amount": 11000, "Currency": "CAD",
                             "Description": "Large Withdrawal"}

        # Act
        self.data_processor.check_suspicious_transactions(large_amount)

        # Assert
        self.assertIn(large_amount, self.data_processor._suspicious_transactions)


    def test_check_suspicious_transactions_uncommon_currency(self):
        # Arrange
        uncommon_currency = {"Transaction ID": "3", "Account number": "1001", "Date": "2023-03-02",
                                  "Transaction type": "withdrawal", "Amount": 500, "Currency": "XRP",
                                  "Description": "Withdrawal in Uncommon Currency"}

        # Act
        self.data_processor.check_suspicious_transactions(uncommon_currency)

        # Assert
        self.assertIn(uncommon_currency, self.data_processor._suspicious_transactions)


    def test_update_transaction_statistics(self):
        # Arrange
        data_withdrawal = {"Transaction ID": "3", "Account number": "1001", "Date": "2023-03-02",
                           "Transaction type": "withdrawal", "Amount": 500, "Currency": "CAD",
                           "Description": "Groceries"}

        # Act
        self.data_processor.update_transaction_statistics(self.INPUT_DATA[0])  
        self.data_processor.update_transaction_statistics(data_withdrawal)  

        # Assert
        statistics = self.data_processor._transaction_statistics["withdrawal"]
        self.assertEqual(statistics["total_amount"], 500)
        self.assertEqual(statistics["transaction_count"], 1)


    def test_get_average_transaction_amount(self):
        # Arrange
        data_processor = DataProcessor([])
        row = {'Transaction type': 'deposit', 'Amount': '100'}
        data_processor.update_transaction_statistics(row)

        # Act
        average = data_processor.get_average_transaction_amount('deposit')

        # Assert
        self.assertEqual(average, 100)





        




if __name__ == "__main__":
    unittest.main()
