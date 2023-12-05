import csv
import json

class InputHandler:
    """
    This class manages and returns input data of CSV and JSON files.
    """
    def __init__(self, file_path: str):
        """
        Initializes the file path of the file inputted.

        Args: 
            file_path (str): The file path of the input.
        """
        self._file_path = file_path


    def get_file_format(self) -> str:
        """
        Gets the format of the file specified by the file path.

        Returns:
            The format of the file.
        """
        return self._file_path.split('.')[-1]

    def read_input_data(self) -> list:
        """
        Reads the data of the CSV or JSON file specified by the file path.

        Returns:
            A list containing data from the CSV or JSON file after data validation.         
        """
        data = []
        file_format = self.get_file_format()
        if file_format == 'csv':
            data =  self.read_csv_data()
        elif file_format == 'json':
            data = self.read_json_data()       
        validated_data = self.data_validation(data)
        return validated_data

    def read_csv_data(self) -> list:
        """
        Reads data of the CSV file specified by the file path.

        Raises:
            FileNotFoundError: Raised if the file path does not exist.

        Returns: 
            A list of dictionaries containing data from the CSV file.
        """
        input_data = []
        try:
            with open(self._file_path, 'r') as input_file:
                reader = csv.DictReader(input_file)
                for row in reader:
                    input_data.append(row)
            return input_data
        except FileNotFoundError:
            raise FileNotFoundError(f"File: {self._file_path} does not exist.")      

    def read_json_data(self) -> list:
        """
        Reads data of the JSON file specified by the file path.

        Raises: 
            FileNotFoundError: Raised if the file path does not exist.
        
        Returns:
            A list containing data loaded from the JSON file.
        """
        input_data = []
        try:
            with open(self._file_path, 'r') as input_file:
                input_data = json.load(input_file)
            return input_data
        except FileNotFoundError:
            raise FileNotFoundError(f"File: {self._file_path} does not exist.")

    def data_validation(self, data: list):
        """
        Validates input data from the read_input_data method.

        Args: 
            data (list): A list of dictionaries produced by the read_input_data method.

        Raises:
            ValueError: Raised if the transaction amount is not a non-negative float.
            TypeError: Raised if the transaction type is not a valid transaction type.

        Returns:
            A list of dictionaries containing only valid data.        
        """
        valid_data = []
        valid_amount = False
        valid_type = False
        for row in data:
            try:
                # TRANSACTION AMOUNT VALIDATION
                transaction_amount = float(row['Amount'])
                if transaction_amount >= 0:
                    valid_amount = True
                else:
                    valid_amount = False
            except ValueError:
                continue
            try:
                # TRANSACTION TYPE VALIDATION
                transaction_type = str(row['Transaction type'])
                if transaction_type in ['deposit', 'withdrawal', 'transfer']:
                    valid_type = True
                else:
                    valid_type = False
            except TypeError:
                continue            
            if valid_amount and valid_type:
                valid_data.append(row)
        return valid_data