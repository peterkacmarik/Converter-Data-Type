# Import necessary libraries
from convert_data_manager import DataManager, Converter, ExportData
# Use pandasgui for interactive data exploration (optional, comment out if not used)
from pandasgui import show
from io_buffer import BufferManager
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
            converted_data = bytes_buffer_manager.read_bytes_buffer()
        elif show_output_format == 'xlsx':
            converted_data = xlsx_buffer_manager.read_buffer_xlsx()
        elif show_output_format in list_allowed_extensions:
            converted_data = string_buffer_manager.read_string_buffer()
        return converted_data

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
        suffix = re.findall(pattern, output_file_path)[0]
    
        # Check if the found file extension matches the specified export format
        if suffix == export_output_format:
            # Create an instance of ExportData to handle the export process
            export_data_manager = ExportData(df_load_data, export_output_format, output_file_path)
            
            # Perform the data export
            export_data_manager.export_data()
        else:
            # Raise a ValueError if the found file extension does not match the specified export format
            raise ValueError("Incorrect export format.")


    # --- Main execution flow --- #
    
    # Initialize buffer managers for different data types
    bytes_buffer_manager = BufferManager()
    xlsx_buffer_manager = BufferManager()
    string_buffer_manager = BufferManager()
    
    # Define input file path and desired output format
    input_file = 'converter_2.0/dataset/mock_data.xml'
    show_output_format = 'csv'  # Options for XML: 'latin-1', 'ISO-8859-2', 'windows-1252', 'windows-1250'
    
    # --- View output data functionality --- #
    
    file_data_manager = load_input_file(input_file)
    df_load_data = create_dataframe(file_data_manager)
    convert_data_to_buffer(df_load_data)
    result = show_convert_data()
    # print(result)
    # gui = show(df_load_data)

    # --- Export functionality commented out for now --- #
    
    # Define output file path and format
    # output_file_path = 'converter_2.0/dataset/test_export.json'
    # export_output_format = 'json'
    # export_file(output_file_path, export_output_format)