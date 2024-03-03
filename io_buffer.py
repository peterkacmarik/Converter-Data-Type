# Import pandas library for data manipulation
import pandas as pd

# Import BytesIO and StringIO from io library for memory buffers
from io import BytesIO, StringIO


# Define a class to manage different buffer types
class BufferManager:
    """
    This class manages three different buffers: bytes buffer, xlsx buffer, and string buffer.
    It provides methods to read data from each buffer.
    """

    # Set default encoding for reading data
    data_decoding = 'windows-1252'

    # Initialize the class with empty buffers
    def __init__(self):
        """
        Initializes the buffers with empty memory objects.
        """
        self.bytes_buffer = BytesIO()
        self.xlsx_buffer = BytesIO()
        self.string_buffer = StringIO()

    # Read and decode the contents of the bytes buffer
    def read_bytes_buffer(self):
        """
        Reads data from the bytes buffer, decodes it using the specified encoding, and returns it as a string.
        """
        # Reset the buffer position to the beginning
        self.bytes_buffer.seek(0)  # Reset the read pointer to the beginning
        # Read all bytes from the buffer
        data = self.bytes_buffer.read() #.decode(self.data_decoding)
        # Decode the bytes using the specified encoding
        result = data.decode(self.data_decoding)
        return result

     # Read and load the contents of the Excel buffer as a Pandas DataFrame
    def read_buffer_xlsx(self):
        """
        Reads data from the xlsx buffer as an Excel spreadsheet using the openpyxl engine and returns a pandas DataFrame.
        """
        # Reset the buffer position to the beginning
        self.xlsx_buffer.seek(0)  # Reset the read pointer to the beginning
        # Use Pandas with the `openpyxl` engine to read the Excel data
        result = pd.read_excel(self.xlsx_buffer, engine='openpyxl')
        return result

    # Read the contents of the string buffer
    def read_string_buffer(self):
        """
        Reads data from the string buffer and returns it as a string.
        """
        # Reset the buffer position to the beginning
        self.string_buffer.seek(0)  # Reset the read pointer to the beginning
        # Read all text from the buffer
        result = self.string_buffer.read()
        return result

    
    # def reset_buffer(self):
    #     self.bytes_buffer.seek(0)
    #     self.bytes_buffer.truncate(0)
        
    #     self.xlsx_buffer.seek(0)
    #     self.xlsx_buffer.truncate(0)
        
    #     self.string_buffer.seek(0)
    #     self.string_buffer.truncate(0)