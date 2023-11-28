class DataProcessor:
    """
    Handles data input to generate the transactions and identify doubtful ones.
    """

    LARGE_TRANSACTION_THRESHOLD = 10000
    UNCOMMON_CURRENCIES = ['XRP', 'LTC']

    def __init__(self, input_data: list):
        """
        Uses input data to initialize the Data Processor.

        Args:
        input_data (list): List of dictionaries having transaction data.
        """
        self._input_data = input_data
        self._account_summaries = {}
        self._suspicious_transactions = []
        self._transaction_statistics = {}

    def process_data(self) -> dict:
        """
        Calculates transaction statistics, finds doubtful transactions, and generates account summaries by processing input data.

        Returns:
        dict: Having account summaries, doubtful transactionns and transaction statistics.
        """
        for row in self._input_data:
            self.update_account_summary(row)
            self.check_suspicious_transactions(row)
            self.update_transaction_statistics(row)

        return {
            "account_summaries": self._account_summaries,
            "suspicious_transactions": self._suspicious_transactions,
            "transaction_statistics": self._transaction_statistics
        }

    def update_account_summary(self, row: dict) -> None:
        """
        Accounts summaries are updated with transaction data.

        Args:
        row (dict): Dictionary formatted transaction data.
        """
        account_number = row['Account number']
        transaction_type = row['Transaction type']
        amount = float(row['Amount'])

        if account_number not in self._account_summaries:
            self._account_summaries[account_number] = {
                "account_number": account_number,
                "balance": 0,
                "total_deposits": 0,
                "total_withdrawals": 0
            }

        if transaction_type == "deposit":
            self._account_summaries[account_number]["balance"] += amount
            self._account_summaries[account_number]["total_deposits"] += amount
        elif transaction_type == "withdrawal":
            self._account_summaries[account_number]["balance"] -= amount
            self._account_summaries[account_number]["total_withdrawals"] += amount

    def check_suspicious_transactions(self, row: dict) -> None:
        """
        checking for doubtful transactions based on amount and currency.

        Args:
        row (dict): Dictionary formatted transaction data.
        """
        amount = float(row['Amount'])
        currency = row['Currency']

        if amount > self.LARGE_TRANSACTION_THRESHOLD or currency in self.UNCOMMON_CURRENCIES:
            self._suspicious_transactions.append(row)

    def update_transaction_statistics(self, row: dict) -> None:
        """
        Updates transaction statistics useing the transaction data.

        Args: 
        row (dict): Dictionary formatted transaction data.
        """
        transaction_type = row['Transaction type']
        amount = float(row['Amount'])

        if transaction_type not in self._transaction_statistics:
            self._transaction_statistics[transaction_type] = {
                "total_amount": 0,
                "transaction_count": 0
            }

        self._transaction_statistics[transaction_type]["total_amount"] += amount
        self._transaction_statistics[transaction_type]["transaction_count"] += 1

    def get_average_transaction_amount(self, transaction_type: str) -> float:
        """
        Calculates the average transaction amount of the given transaction.

        Args: 
        Transaction_type (str): Type of transaction.

        Returns: 
        float: Average transaction amount.
        """
        total_amount = self._transaction_statistics[transaction_type]["total_amount"]
        transaction_count = self._transaction_statistics[transaction_type]["transaction_count"]

        if transaction_count == 0:
            average = 0
        else:
            average = total_amount / transaction_count
        
        return average
