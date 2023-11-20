import csv

class OutputHandler:
    """
    REQUIRED: CLASS DOCSTRING
    """

    def __init__(self, account_summaries: dict, 
                       suspicious_transactions: list, 
                       transaction_statistics: dict) -> None:
        """
        REQUIRED: METHOD DOCSTRING
        """
        self._account_summaries = account_summaries
        self._suspicious_transactions = suspicious_transactions
        self._transaction_statistics = transaction_statistics
    

    def write_account_summaries_to_csv(self, file_path: str) -> None:
        """
        REQUIRED: METHOD DOCSTRING
        """
        with open(file_path, 'w', newline='') as output_file:
            writer = csv.writer(output_file)
            writer.writerow(['Account number', 'Balance', 'Total Deposits', 'Total Withdrawals'])

            for account_number, summary in self._account_summaries.items():
                writer.writerow([
                    account_number,
                    summary['balance'],
                    summary['total_deposits'],
                    summary['total_withdrawals']
                ])

    def write_suspicious_transactions_to_csv(self, file_path: str) -> None:
        """
        REQUIRED: METHOD DOCSTRING
        """
        with open(file_path, 'w', newline='') as output_file:
            writer = csv.writer(output_file)
            writer.writerow(['Transaction ID', 'Account number', 'Date', 'Transaction type', 'Amount', 'Currency', 'Description'])

            for transaction in self._suspicious_transactions:
                writer.writerow([
                    transaction['Transaction ID'],
                    transaction['Account number'],
                    transaction['Date'],
                    transaction['Transaction type'],
                    transaction['Amount'],
                    transaction['Currency'],
                    transaction['Description']
                ])

    def write_transaction_statistics_to_csv(self, file_path: str) -> None:
        """
        REQUIRED: METHOD DOCSTRING
        """        
        with open(file_path, 'w', newline='') as output_file:
            writer = csv.writer(output_file)
            writer.writerow(['Transaction type', 'Total amount', 'Transaction count'])

            for transaction_type, statistic in self._transaction_statistics.items():
                writer.writerow([
                    transaction_type,
                    statistic['total_amount'],
                    statistic['transaction_count']
                ])