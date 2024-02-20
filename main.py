# Import necessary libraries
from convert_data_manager import DataManager, Converter, ExportData
# Use pandasgui for interactive data exploration (optional, comment out if not used)
from pandasgui import show
from io_buffer import BufferManager
from features import AdvancedFeatures
from tabulate import tabulate

# Execute code only when script is run directly, not imported as a module
if __name__ == '__main__':
    
    # Define input file path, URL, and desired output format
    input_file = 'dataset/iris.csv'
    input_url = 'https://www.worldometers.info/geography/alphabetical-list-of-countries/'
    show_output_format = 'json'
    
    # Initialize buffer managers for different data types
    bytes_buffer_manager = BufferManager()
    xlsx_buffer_manager = BufferManager()
    string_buffer_manager = BufferManager()

    # Function to load data from a file
    def manager_input_file(input_file: str):
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
        list_format = {'csv', 'json', 'html', 'md', 'tex'}

        if show_output_format == 'xml':
            converted_data = bytes_buffer_manager.read_bytes_buffer()
        elif show_output_format == 'xlsx':
            converted_data = xlsx_buffer_manager.read_buffer_xlsx()
        elif show_output_format in list_format:
            converted_data = string_buffer_manager.read_string_buffer()
        return converted_data

    # Function to export converted data to a file (commented out for now)
    def export_file():
        """
        Exports the converted data to a specified file.

        This function is currently commented out, but can be uncommented to 
        enable data export functionality.

        Args:
            None
        """
        # Define output file path and format
        output_file_path = 'converter_2.0/dataset/mock_data.md'
        export_output_format = 'md'
        
        # Create a DataFrame from the data loaded from the input file.
        df_load_data = create_dataframe(file_data_manager=manager_input_file(input_file))

         # Create an ExportData instance to handle the export
        export_data_manager = ExportData(df_load_data, export_output_format, output_file_path)
        
        # Perform the data export
        export_data_manager.export_data()

    # Main execution flow
    file_data_manager = manager_input_file(input_file)
    df_load_data = create_dataframe(file_data_manager)
    convert_data_to_buffer(df_load_data)
    result = show_convert_data()
    # gui = show(df_load_data)
    
    # Export functionality commented out for now
    # export_file()