# Import classes and modules for data conversion management
from convert_data_manager import DataManager, Converter, ExportData

# Import the show function from the pandasgui module to display the interactive GUI for the pandas DataFrame
# from pandasgui import show

# Import the BufferManager class from the io_buffer file to manage input and output
from io_buffer import BufferManager

# Import the re module for working with regular expressions
import re


# Execute code only when script is run directly, not imported as a module
if __name__ == '__main__':
    # Function to load data from a file
    def load_input_file(input_file: str):
        """
        Initializes the data loading class based on file type (csv, json, xml, xlsx, html).
        Args:
            input_file (str): Path to the input file.
        Returns:
            DataManager: Instance of the data loading class.
        """
        file_data_manager = DataManager(input_file)
        return file_data_manager

    # Function to create a DataFrame from loaded data
    def create_dataframe(file_data_manager: DataManager):
        """
        Loads data from a file and creates a Pandas DataFrame.
        Args:
            file_data_manager (DataManager): Instance of the data loading class.
        Returns:
            pd.DataFrame: Pandas DataFrame containing the loaded data.
        """
        df_load_data = file_data_manager.load_data()
        return df_load_data

    # Function to convert data to specified format and store in buffers
    def convert_data_to_buffer(df_load_data):
        """
        Initializes the data conversion class and converts the DataFrame to the desired format.
        Args:
            df_load_data (pd.DataFrame): Pandas DataFrame to be converted.
        """
        file_converter = Converter(
            df_load_data,
            show_output_format,
            bytes_buffer_manager.bytes_buffer,
            xlsx_buffer_manager.xlsx_buffer,
            string_buffer_manager.string_buffer,
        )
        file_converter.convert_data()

    # Function to read and display converted data based on the output format
    def show_convert_data():
        """
        Reads the converted data from the appropriate buffer and returns it.
        Returns:
            str or pd.DataFrame: The converted data in the specified format.
        """
        list_allowed_extensions = ['csv', 'json', 'html', 'md', 'tex']
        
        if show_output_format == 'xml':
            return bytes_buffer_manager.read_bytes_buffer()
        elif show_output_format == 'xlsx':
            return xlsx_buffer_manager.read_buffer_xlsx()
        elif show_output_format in list_allowed_extensions:
            return string_buffer_manager.read_string_buffer()

    # Function to export converted data to a file (commented out for now)
    def export_file(output_file_path, export_output_format):
        """
        Exports the data to a file in the specified format.

        Args:
            output_file_path (str): The path to the output file.
            export_output_format (str): The desired output format.

        Raises:
            ValueError: If the file extension does not match the specified export format.
        """
        # Regular expression pattern to extract the file extension
        pattern = r'([a-z]+)$'
        suffix = re.search(pattern, output_file_path)[0]
    
        # Check if the found file extension matches the specified export format
        if suffix == export_output_format:
            # Create an instance of ExportData to handle the export process
            export_data_manager = ExportData(df_load_data, export_output_format, output_file_path)
            
            # Perform the data export
            export_data_manager.export_data()
        else:
            # Raise a ValueError if the found file extension does not match the specified export format
            raise ValueError(f"Incorrect export format. Expected {export_output_format}, got {suffix}.")


    # --- Main execution flow --- #
    
    # Initialize buffer managers for different data types
    bytes_buffer_manager = BufferManager()
    xlsx_buffer_manager = BufferManager()
    string_buffer_manager = BufferManager()
    
    # Define input file path and desired output format
    input_file = 'dataset/mock_data.html'
    show_output_format = 'csv'
    
    # --- View output data functionality --- #
    
    file_data_manager = load_input_file(input_file)
    df_load_data = create_dataframe(file_data_manager)
    convert_data_to_buffer(df_load_data)
    result = show_convert_data()
    print(result)
    # gui = show(df_load_data)

    # --- Export functionality commented out for now --- #
    
    # Define output file path and format
    # output_file_path = 'dataset/test_export_file.csv'
    # export_output_format = 'csv'
    # export_file(output_file_path, export_output_format)
