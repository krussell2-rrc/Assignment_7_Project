import csv

class OutputHandler:
    """
    This class handles and exports transactional data to CSV file.
    """

    def __init__(self, account_summaries: dict, 
                       suspicious_transactions: list, 
                       transaction_statistics: dict) -> None:
        
        """
            Initialize the OutputHandler instance using the account summaries, 
        suspicious transactions and transaction statistics.

        Args:
            account_summaries (dict) : A dictionary to store the summary of accounts.
            suspicious_transactions (list) : A list to store suspicious transactions.
            transaction_statistics (dict) : A dictionary to store transaction statistics.

        Returns:
            None
        """
        self._account_summaries = account_summaries
        self._suspicious_transactions = suspicious_transactions
        self._transaction_statistics = transaction_statistics
    
    def write_account_summaries_to_csv(self, file_path: str) -> None:
        """
        This method writes the account summaries to the CSV file.

        Args:
            file_path (str) : The path of the CSV file.

        Returns:
            None 
        """

        with open(file_path, 'w', newline='') as output_file:
            writer = csv.writer(output_file)
            writer.writerow(['Account number', 'Balance', 'Total Deposits', 'Total Withdrawals'])

            # Write account summaries to the CSV file.
            for account_number, summary in self._account_summaries.items():
                writer.writerow([
                    account_number,
                    summary['balance'],
                    summary['total_deposits'],
                    summary['total_withdrawals']
                ])

    def write_suspicious_transactions_to_csv(self, file_path: str) -> None:
        """
        This method writes the suspicious transactions to the CSV file.

        Args:
            file_path (str) : The path of the CSV file.

        Returns:
            None
        """

        with open(file_path, 'w', newline='') as output_file:
            writer = csv.writer(output_file)
            writer.writerow(['Transaction ID', 'Account number', 'Date', 'Transaction type', 'Amount', 'Currency', 'Description'])

            # Write suspicious transactions to the CSV file.
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
        This method writes the transaction statistics to the CSV file.

        Args:
            file_path (str) : The path of the CSV file.

        Returns:
            None
        """    

        with open(file_path, 'w', newline='') as output_file:
            writer = csv.writer(output_file)
            writer.writerow(['Transaction type', 'Total amount', 'Transaction count'])

            # Write transaction statistics to the CSV file.
            for transaction_type, statistic in self._transaction_statistics.items():
                writer.writerow([
                    transaction_type,
                    statistic['total_amount'],
                    statistic['transaction_count']])

    def filter_account_summaries(self, filter_field: str, filter_value: int, filter_mode: bool) -> list:
        """
        This method filter the account summaries based on the provided criteria.

        Args:
            filter field (string): One of the following filter fields: "balance","total_deposits" or "total_withdrawals".
            filter value (integer): An integer value to which the filter field will be compared.
            filter mode (boolean): True: Greater than or Equal, False: Less than or Equal.
        Returns:
            list : filtered_account_summaries
        """
        filtered_account_summaries = []
        
        for account_number, summary in self._account_summaries.items():
            field_value = summary.get(filter_field, 0)

            if (filter_mode and field_value >= filter_value) or (not filter_mode and field_value <= filter_value):
                filtered_account_summaries.append({"Account number": account_number,"Balance": summary["balance"],
                "Total Deposits": summary["total_deposits"],"Total Withdrawals": summary["total_withdrawals"]})

        return filtered_account_summaries
    
    def write_filtered_account_summaries_to_csv(self, filtered_data: list, file_path: str) -> None:
        """
        This method writes the filtered account summaries to CSV file.

        Args:
            filtered_data (list) : A list of filtered account summaries.
            file_path (str) : The path of the CSV file.

        Returns:
            None
        """
        with open(file_path, 'w', newline='') as output_file:
            data = csv.writer(output_file)
            data.writerow(['Account number', 'Balance', 'Total Deposits', 'Total Withdrawals'])

            for summary in filtered_data:
                data.writerow([summary['Account number'],summary['Balance'],summary['Total Deposits'],summary['Total Withdrawals']])
                

