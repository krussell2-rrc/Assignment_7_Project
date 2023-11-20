import csv
import json

class InputHandler:
    """
    This class manages and returns input data of csv and json files.
    """
    def __init__(self, file_path: str):
        """
        Initializes the file path of the file inputted.

        Args: 
            file_path (str): The file path of the input.

        Raises: 
            None 
        """
        self._file_path = file_path


    def get_file_format(self) -> str:
        """
        Returns the format of the file inputted.

        Raises:
            None
        """
        return self._file_path.split('.')[-1]

    def read_input_data(self) -> list:
        """
        Reads and returns the data of the csv or json file inputted.

        Raises:
            None        
        """
        data = []
        file_format = self.get_file_format()
        if file_format == 'csv':
            data =  self.read_csv_data()
        elif file_format == 'json':
            data = self.read_json_data()
        return data

    def read_csv_data(self) -> list:
        """
        Reads and returns data of csv files inputted.

        Raises:
            FileNotFoundError: Raised if the file path does not exist.
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
        Reads and returns data of json files inputted.

        Raises: 
            FileNotFoundError: Raised if the file path does not exist.
        """
        # Research the json.load function so that you 
        # understand the format of the data once it is
        # placed into input_data
        input_data = []
        try:
            with open(self._file_path, 'r') as input_file:
                input_data = json.load(input_file)
            return input_data
        except FileNotFoundError:
            raise FileNotFoundError(f"File: {self._file_path} does not exist.")
