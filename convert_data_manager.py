import pandas as pd
import markdown

class DataManager:
    # Default encoding for data loading and export
    data_encoding = 'utf-8'
    
    def __init__(self, input_file: str) -> None:
        """
        Initializes the DataManager class with the input file path.

        Args:
            input_file (str): Path to the input file.
        """
        self.input_file = input_file
        # Allowed file extensions for loading
        self.allowed_extensions = ['csv', 'json', 'xml', 'xlsx', 'html', 'md', 'tex']
        
    def allowed_file(self):
        """
        Checks if the input file has a supported extension.

        Returns:
            bool: True if the extension is allowed, False otherwise.
        """
        # Check if the file has an extension and if it's in the allowed list
        return '.' in self.input_file and self.input_file.rsplit('.', 1)[1].lower() in self.allowed_extensions
        
    def load_data(self):
        """
        Loads data from the input file based on its extension.

        Returns:
            pd.DataFrame or None: The loaded data as a DataFrame if successful, None otherwise.
        """
        df_result = None  # Initialize result variable
        
        try:
            # Try loading based on file extension
            if self.input_file.endswith('.csv') and self.allowed_file():
                df_result = pd.read_csv(self.input_file)
            elif self.input_file.endswith('.json') and self.allowed_file():
                df_result = pd.read_json(self.input_file, encoding=self.data_encoding).round(2)
            elif self.input_file.endswith('.xml') and self.allowed_file():
                df_result = pd.read_xml(self.input_file, encoding=self.data_encoding)
            elif self.input_file.endswith('.xlsx') and self.allowed_file():
                df_result = pd.read_excel(self.input_file)
            elif self.input_file.endswith('.html') and self.allowed_file():
                list_df_result = pd.read_html(self.input_file, encoding=self.data_encoding)
                df_result = list_df_result[0]
            else:
                # Raises a ValueError if the output format is not supported
                raise ValueError("Load Data - Unsupported file type.")
            
            return df_result
        
        # Handle specific errors raised during loading
        except pd.errors.EmptyDataError:
            print("Error: An empty file.")
        except (FileNotFoundError, pd.errors.ParserError) as e:
            print(f"Error: {e}")

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
            # Checking if the loaded data is a DataFrame
            if isinstance(self.df_load_data, pd.DataFrame):
                # Convert data based on output format
                if self.output_format == 'csv':
                    self.df_load_data.to_csv(self.string_buffer, index=False)
                elif self.output_format == 'json':
                    self.df_load_data.to_json(self.string_buffer, orient='records', indent=4, index=False)
                elif self.output_format == 'xml':
                    self.df_load_data.columns = self.df_load_data.columns.str.replace(' ', '_')
                    self.df_load_data.to_xml(self.bytes_buffer, index=False)
                elif self.output_format == 'xlsx':
                    self.df_load_data.to_excel(self.xlsx_buffer, index=False)
                elif self.output_format == 'html':
                    # self.df_load_data.columns = self.df_load_data.columns.str.replace(' ', '_')
                    self.df_load_data.to_html(self.string_buffer, index=False)
                elif self.output_format == 'md':
                    self.df_load_data.to_markdown(self.string_buffer, index=False)  # tablefmt="grid"
                elif self.output_format == 'tex':
                    self.df_load_data.to_latex(self.string_buffer, index=False)
                
                # Handle unsupported output formats
                elif self.output_format not in ['csv', 'json', 'xml', 'xlsx', 'html', 'md', 'tex']:
                    raise ValueError(f"Invalid output format: {self.output_format}")
            
            # Handle non-DataFrame data
            else:
                raise TypeError("A DataFrame is expected.")
        
        except TypeError as e:
            print(f"Chyba: {e}")

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
            # Check if the data is a DataFrame
            if isinstance(self.df_load_data, pd.DataFrame):
                try:
                    # Export data based on output format
                    if self.export_output_format == 'csv':
                        self.df_load_data.to_csv(self.output_file_path, index=False)
                    elif self.export_output_format == 'json':
                        self.df_load_data.to_json(self.output_file_path, orient='records', indent=2, index=False)
                    elif self.export_output_format == 'xml':
                        self.df_load_data.to_xml(self.output_file_path, index=False)
                    elif self.export_output_format == 'xlsx':
                        self.df_load_data.to_excel(self.output_file_path, index=False)
                    elif self.export_output_format == 'html':
                        self.df_load_data.to_html(self.output_file_path, index=False)
                    elif self.export_output_format == 'md':
                        self.df_load_data.to_markdown(self.output_file_path, index=False)
                    elif self.export_output_format == 'tex':
                        self.df_load_data.to_latex(self.output_file_path, index=False)
                
                # Handle unsupported output formats
                except ValueError as ve:
                        # If a ValueError occurs during export, it prints an error message
                    print(ve)
            
            # Handle non-DataFrame data
            else:
                # If the data loaded is not a DataFrame, it throws a ValueError
                raise ValueError("Export - Incorrect input data format.")
        
        except ValueError as ve:
                # If a ValueError occurs during data processing, it prints an error message
            print(ve)