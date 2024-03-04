# Import the re library, pandas library and assign it the alias pd
import pandas as pd

# Import the re module for working with regular expressions
import re

# Import function is_valid_mime_type from module valid_mime_type
from valid_mime_type import is_valid_mime_type


class DataManager:
    """
    The DataManager class is used for managing and manipulating data loaded from a file.
    """
    # Default encoding for data loading and export
    data_encoding = 'utf-8'

    def __init__(self, input_file: str) -> None:
        """
        Initializes the DataManager class with the input file path.

        Args:
            input_file (str): Path to the input file.
        """
        self.input_file = input_file

    def extract_suffix(self) -> str:
        """
        Extracts the file extension from the given file name.

        Returns:
            str: The extracted file extension.
        """
        pattern = r'(\.[a-z]+)$'
        found_suffix = re.search(pattern, self.input_file)[0]  
        return found_suffix
        
    def load_data(self):
        """
        Loads data from the input file based on its extension.

        Returns:
            pd.DataFrame or None: The loaded data as a DataFrame if successful, None otherwise.
        """
        try:
            # Extracts the file extension using the extract_suffix() method
            suffix = self.extract_suffix()

            # Checks the validity of the file's MIME type using the is_valid_mime_type() function
            if is_valid_mime_type(suffix, self.input_file):
                # If the MIME type is valid, uses a match construct based on the file extension
                match suffix:
                    # If the extension is '.csv', reads the data from the file as CSV using the read_csv() method
                    case '.csv':
                        return pd.read_csv(self.input_file)
                    # If the extension is '.json', reads the data from the file as JSON using the read_json() method
                    case '.json':
                        return pd.read_json(self.input_file).round(2)
                    # If the extension is '.xml', reads the data from the file as XML using the read_xml() method
                    case '.xml':
                        return pd.read_xml(self.input_file)
                    # If the extension is '.xlsx', reads the data from the file as Excel using the read_excel() method
                    case '.xlsx':
                        return pd.read_excel(self.input_file)
                    # If the extension is '.html', reads the data from the file as HTML using the read_html() method
                    case '.html':
                        list_df_result = pd.read_html(self.input_file)
                        return list_df_result[0]
                    # If the extension does not match any supported formats, raises an exception
                    case _:
                        raise ValueError("Load Data: Unsupported file type.")
            else:
                # If the file's MIME type is not valid, raises an exception
                raise ValueError("The file extension is not supported. Invalid MIME type.")
            
        # Handle specific errors raised during loading
        except pd.errors.EmptyDataError:
            print("Load Error: An empty file.")
        except (FileNotFoundError, pd.errors.ParserError) as e:
            print(f"Load Error: {e}")
        # Catches exceptions in case of problems with loading data from the file
        except ValueError as ve:
            # Prints the error message
            print(f"Load Error: {ve}")
            
class Converter:
    def __init__(self, df_load_data: pd.DataFrame, output_format: str, bytes_buffer, xlsx_buffer, string_buffer) -> None:
        """
        Initializes the Converter class with data, output format, and buffers.

        Args:
            df_load_data (pd.DataFrame): Pandas DataFrame to be converted.
            output_format (str): Desired output format.
            bytes_buffer: Buffer for bytes data.
            xlsx_buffer: Buffer for Excel data.
            string_buffer: Buffer for string data.
        """
        self.df_load_data = df_load_data
        self.output_format = output_format
        self.bytes_buffer = bytes_buffer
        self.xlsx_buffer = xlsx_buffer
        self.string_buffer = string_buffer

    def convert_data(self):
        """
        Converts the loaded data to the specified format and stores it in the appropriate buffer.
        """
        try:
            if isinstance(self.df_load_data, pd.DataFrame):
                # Check if the loaded data is a Pandas DataFrame
                match self.output_format:
                    # Using the match construct to handle different output formats
                    case 'csv':
                        # If the output format is CSV, write the DataFrame to a CSV file
                        self.df_load_data.to_csv(self.string_buffer, index=False)
                    case 'json':
                        # If the output format is JSON, write the DataFrame to a JSON file
                        self.df_load_data.to_json(self.string_buffer, orient='records', indent=4, index=False)
                    case 'xml':
                        # If the output format is XML, convert DataFrame to XML and write to buffer
                        self.df_load_data.columns = self.df_load_data.columns.str.replace(' ', '_')
                        self.df_load_data.to_xml(self.bytes_buffer, index=False)
                    case 'xlsx':
                        # If the output format is XLSX, write the DataFrame to an Excel file
                        self.df_load_data.to_excel(self.xlsx_buffer, index=False)
                    case 'html':
                        # If the output format is HTML, write the DataFrame to an HTML file
                        # self.df_load_data.columns = self.df_load_data.columns.str.replace(' ', '_')
                        self.df_load_data.to_html(self.string_buffer, index=False)
                    case 'md':
                        # If the output format is Markdown, write the DataFrame to a Markdown file
                        self.df_load_data.to_markdown(self.string_buffer, index=False)
                    case 'tex':
                        # If the output format is TeX, write the DataFrame to a LaTeX file
                        self.df_load_data.to_latex(self.string_buffer, index=False)
                    case _:
                        # If the output format is not recognized, raise a ValueError
                        raise ValueError(f"Invalid output format: {self.output_format}")
            else:
                # Throws an exception if the data loaded is not a DataFrame
                raise ValueError("A DataFrame is expected, check the validity of the input data.")  

        except ValueError as ve:
            # If a ValueError occurs during data processing, it prints an error message
            print(f"Convert Error: {ve}")

class ExportData:
    def __init__(self, df_load_data: pd.DataFrame, export_output_format: str, output_file_path) -> None:
        """
        Initializes the ExportData class with data, output format, and output file path.

        Args:
            df_load_data (pd.DataFrame): Pandas DataFrame to be exported.
            export_output_format (str): Desired output format.
            output_file_path (str): Path to the output file.
        """
        self.df_load_data = df_load_data
        self.export_output_format = export_output_format
        self.output_file_path = output_file_path
    
    def export_data(self):
        """
        Exports the data to a file in the specified format.
        """
        try:
            if isinstance(self.df_load_data, pd.DataFrame):
                # Checking the type of input data, whether it is a DataFrame
                match self.export_output_format:
                    # For supported output formats cases
                    case 'csv':
                        # Export to CSV format
                        self.df_load_data.to_csv(self.output_file_path, index=False)
                    case 'json':
                        # Export to JSON format
                        self.df_load_data.to_json(self.output_file_path, orient='records', indent=2, index=False)
                    case 'xml':
                        # Export to XML format
                        self.df_load_data.to_xml(self.output_file_path, index=False)
                    case 'xlsx':
                        # Export to Excel format
                        self.df_load_data.to_excel(self.output_file_path, index=False)
                    case 'html':
                        # Export to HTML format
                        self.df_load_data.to_html(self.output_file_path, index=False)
                    case 'md':
                        # Export to Markdown format
                        self.df_load_data.to_markdown(self.output_file_path, index=False)
                    case 'tex':
                        # Export to LaTeX format
                        self.df_load_data.to_latex(self.output_file_path, index=False)
                    case _:
                        # Executed if the specified format does not match the supported formats
                        raise ValueError(f"Invalid output format: {self.export_output_format}")
            else:
                # Throws an exception if the data loaded is not a DataFrame
                raise ValueError("A DataFrame is expected, check the validity of the input data.")  # Vyvolá výnimku, ak načítané dáta nie sú DataFrame            

        except ValueError as ve:
            # If a ValueError occurs during data processing, it prints an error message
            print(f"Export Error: {ve}")
