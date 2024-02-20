# Data Converter

## Description

This repository contains a set of scripts and tests for data manipulation.

The Data Converter is a Python program designed to load, convert, and export data from various file formats. It supports the conversion of data to formats such as CSV, JSON, XML, HTML and XLSX. The program uses the `pandas` library for data manipulation and the `BytesIO` and `StringIO` classes for working with binary and text data.

*Features:*
- Support for multiple input and output formats.
- Easy-to-use interface for data conversion.
- Compatibility with common data formats.

## Supported Formats

- **Input Formats:** CSV, JSON, XML, XLSX, HTML
- **Output Formats:** CSV, JSON, XML, XLSX, HTML, Markdown and LaTeX

## Badges

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)](https://www.python.org/downloads/release)
[![Pandas Version](https://img.shields.io/badge/pandas-1.3.3-green.svg)](https://pandas.pydata.org/)
[![Open Issues](https://img.shields.io/github/issues/your-username/your-repository.svg)](https://gitlab.websupport.sk/tgnws/convert/-/issues)

## Visuals

*Screenshot or GIF of the Data Converter in action could be inserted here.*

## Installation

Before running the scripts, make sure you have the following installed:

- pandas: A library for working with data and analysis.
- openpyxl: A library for manipulating the Excel file format.
- lxml: Library for working with XML and HTML.
- pandasgui: Tool for interactive manipulation of data in Pandas DataFrame.
- tabulate: Library for formatting tables.
- Jinja2: A templating system written in Python.

You can install the libraries using the command:

```bash
pip install pandas openpyxl lxml pandasgui tabulate Jinja2
```

## Usage

### Data Loading and Manipulation

1. **Loading data from various formats**: The `DataManager` script allows you to load data from CSV, JSON, XML, Excel and HTML files.
2. **Conversion of Data to Various Formats**: The `Converter` script enables the conversion of Pandas data frames to CSV, JSON, XML, Excel, HTML, Markdown and LaTeX formats.
3. **Export Data to Files**: The `ExportData` script allows you to export data from Pandas data frames to files in CSV, JSON, XML, Excel, HTML, Markdown and LaTeX formats.

### Example of Use

```python
# Imports of necessary classes
from convert_data_manager import DataManager, Converter, ExportData
from io_buffer import BufferManager

# Input file definition
input_file = 'dataset/iris.json'

# Initialization of buffers for different types of data
bytes_buffer_manager = BufferManager()
xlsx_buffer_manager = BufferManager()
string_buffer_manager = BufferManager()

# Loading data from an input file
file_data_manager = DataManager(input_file)
df_load_data = file_data_manager.load_data()

# Data conversion into the required format and storage in buffers
file_converter = Converter(df_load_data, 'xml', bytes_buffer_manager.bytes_buffer, xlsx_buffer_manager.xlsx_buffer, string_buffer_manager.string_buffer)
file_converter.convert_data()

# Display of converted data
result = string_buffer_manager.read_string_buffer()
print(result)
```

### 5. Exporting Data

```python
# Export data to a file (example)
export_data_manager = ExportData(df_load_data, 'csv', 'output_file.csv')
export_data_manager.export_data()
```

## Support

If you encounter any issues or have questions, please open an [issue](https://gitlab.websupport.sk/tgnws/convert/-/issues) on GitLab.

## Roadmap

- Version 1.0: Start aplication
- Version 2.0: Additional input and output formats.
- Version 2.1: Improved error handling.

## Contributing

Contributions are welcome! Check out the [Contribution Guidelines](CONTRIBUTING.md) for details.

## Authors and Acknowledgment

- [Michal Štelmak](https://github.com/your-username) - Project Lead
- [Peter Kaćmarík](https://github.com/your-username) - Project developer

Special thanks to [Contributor 1](https://github.com/contributor-1) and [Contributor 2](https://github.com/contributor-2) for their valuable contributions.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Project Status

**Development Status:** Active
