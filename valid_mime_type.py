from mime_type_csv import ValidateCsv
import mimetypes


def is_valid_mime_type(suffix: str, input_file: str) -> bool:
    """
    Checks whether the given file with a specific extension or MIME type is valid.

    Args:
        suffix (str): The file extension or MIME type.
        input_file (str): The path to the input file.

    Returns:
        bool: True if the file is valid, False otherwise.

    Raises:
        Exception: If the file suffix is invalid.
    """
    # Dictionary defining allowed MIME types for each file suffix
    allowed_mime_type = {
        ".json": [
                "text/json",  # Deprecated
                "application/json"],  # Preferred for mimetypes
        ".xml": ["application/xml", 
                "text/xml"],  # Preferred for mimetypes
        ".xlsx": ["application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"],  # Preferred for mimetypes
        ".html": ["text/html"],  # Preferred for mimetypes
    }

    if suffix == '.csv':
        # Create a ValidateCsv object and initialize it with the input file path
        csv_match = ValidateCsv(input_file)
        
        # Call the validate_csv() method to check the CSV file format
        validate = csv_match.validate_csv()
        
        # Call the check_csv_line() method to verify the number of columns in each row
        line_check = csv_match.check_csv_line()
        
        # Check if both validations (format and column count) are successful
        if validate and line_check:
            return True  # If both conditions are met, return True
        else:
            return False  # If at least one of the conditions is not met, return False

    elif suffix in allowed_mime_type:
        # Guessing the MIME type of the input file
        mime_type = mimetypes.guess_type(input_file)[0]
        
        # Extracting key-value pairs from the allowed_mime_type dictionary where the suffix matches
        key_value = [key_value for key_value in allowed_mime_type.items() if suffix in key_value]
        
        # Extracting values (MIME types) associated with the key (suffix)
        value = [value for value in key_value[0][1] if value == mime_type]
        
        # Checking if the guessed MIME type matches any of the allowed MIME types
        if value[0] == mime_type:
            return True  # If the MIME type is valid, return True
        else:
            return False  # If the MIME type is not valid, return False
    else:
        raise Exception("Invalid file suffix.")  # If the file suffix is not valid, raise an exception