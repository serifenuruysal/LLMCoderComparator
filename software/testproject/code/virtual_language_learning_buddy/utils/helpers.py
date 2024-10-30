```python
import json
import os

def load_json_file(file_path):
    """
    Load a JSON file and return its content as a dictionary.
    
    :param file_path: Path to the JSON file.
    :return: Dictionary containing the JSON data.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: The file {file_path} is not a valid JSON.")
        return None

def save_json_file(data, file_path):
    """
    Save a dictionary as a JSON file.
    
    :param data: Dictionary to save.
    :param file_path: Path to the JSON file.
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    except IOError as e:
        print(f"Error: Unable to write to file {file_path}. {e}")

def ensure_directory_exists(directory_path):
    """
    Ensure that a directory exists. If it does not, create it.
    
    :param directory_path: Path to the directory.
    """
    if not os.path.exists(directory_path):
        try:
            os.makedirs(directory_path)
        except OSError as e:
            print(f"Error: Unable to create directory {directory_path}. {e}")

def validate_language_code(language_code):
    """
    Validate if the provided language code is in the correct format (e.g., 'en', 'fr').
    
    :param language_code: Language code to validate.
    :return: True if valid, False otherwise.
    """
    if isinstance(language_code, str) and len(language_code) == 2:
        return True
    else:
        print(f"Error: Invalid language code '{language_code}'. It should be a two-letter code.")
        return False

def format_progress_report(progress_data):
    """
    Format a user's progress data into a readable string.
    
    :param progress_data: Dictionary containing progress data.
    :return: Formatted string of the progress report.
    """
    report_lines = ["User Progress Report:"]
    for key, value in progress_data.items():
        report_lines.append(f"{key}: {value}")
    return "\n".join(report_lines)
```