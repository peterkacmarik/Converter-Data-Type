# mime_type_csv.py

class CsvMatcher():
    """
    The CsvMatcher class is used for matching CSV files.

    Args:
        input_file (str): The path to the input file.

    Attributes:
        signature (bytes): The signature for CSV files (comma).
        input_file (str): The path to the input file.
    """

    def __init__(self, input_file: str):
        """
        Initializes the CsvMatcher object with the input file.

        Args:
            input_file (str): The path to the input file.
        """
        self.signature = b"\x2C"  # Signature for CSV files (comma)
        self.input_file = input_file


    def match(self, buf: bytes):
        """
        Compares the given buffer with the signature for CSV files.

        Args:
            buf (bytes): The data buffer.

        Returns:
            bool: True if the signature is found in the buffer, otherwise False.
        """
        return self.signature in buf

    def extension(self):
        """
        Returns the file extension for CSV files.

        Returns:
            str: The file extension "csv".
        """
        return "csv"

    def mime(self):
        """
        Returns the MIME type for CSV files.

        Returns:
            str: The MIME type "text/csv".
        """
        return "text/csv"

class ValidateCsv(CsvMatcher):
    """
    The ValidateCsv class inherits from the CsvMatcher class and is used for validating CSV files.

    Args:
        input_file (str): The path to the input file.

    Attributes:
        Inherits attributes from the CsvMatcher class.
    """

    def __init__(self, input_file: str):
        """
        Initializes the ValidateCsv object with the input file.

        Args:
            input_file (str): The path to the input file.
        """
        super().__init__(input_file)

    def check_csv_line(self):
        """
        Checks the number of commas in each line of the CSV file.

        Returns:
            bool: True if all lines have the same number of commas, otherwise False.
        """
        with open(self.input_file, 'r') as f:
            lines = f.readlines()

        comma_count = lines[0].count(',')  # Number of commas in the first line

        # Checks each line
        for line in lines[1:]:
            if line.count(',') != comma_count:
                return False  # Returns False if the number of commas differs
        return True  # Returns True if all lines have the same number of commas

    def validate_csv(self):
        """
        Validates the CSV file by checking its signature and line structure.

        Returns:
            bool: True if the CSV file is valid, otherwise False.
        """
        with open(self.input_file, 'rb') as f:
            content = f.read()

        # Checks if the CSV file signature matches
        is_match = self.match(content)
        
        # Checks if each line of the CSV file has the same number of commas
        is_valid_line = self.check_csv_line()

        # Returns True if both signature and line structure are valid, otherwise False
        return is_match and is_valid_line