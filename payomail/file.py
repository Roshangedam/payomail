import os
import requests
from urllib.parse import urlparse, unquote
from datetime import datetime

def download_file(file_source, max_attachment_size_bytes):
    try:
        if isinstance(file_source, str):
            parsed_url = urlparse(file_source)
            if parsed_url.scheme:
                response = requests.get(file_source)
                response.raise_for_status()  # Raise an exception for HTTP errors

                if response.status_code == 200:
                    file_data = response.content
                    filename = os.path.basename(unquote(parsed_url.path))
                    temp_folder = os.path.join(os.getcwd(), 'payomail', 'temp')
                    os.makedirs(temp_folder, exist_ok=True)
                    file_path = os.path.join(temp_folder, filename)

                    # Check if the file already exists and has the same size
                    if os.path.exists(file_path) and os.path.getsize(file_path) == len(file_data):
                        return {'status': 'Success', 'path': file_path, 'error_message': 'File already exists.'}

                    # Check if the file size exceeds the maximum allowed size
                    if len(file_data) > max_attachment_size_bytes:
                        return {'status': 'Failure', 'path': '', 'error_message': f"File size exceeds the maximum allowed size ({max_attachment_size_bytes} bytes)."}
                    
                    with open(file_path, 'wb') as file:
                        file.write(file_data)

                    return {'status': 'Success', 'path': file_path, 'error_message': ''}
                else:
                    return {'status': 'Failure', 'path': '', 'error_message': f"HTTP error: {response.status_code}"}

            elif os.path.exists(file_source):
                file_path = os.path.abspath(file_source)
                # Check if the file already exists and has the same size
                if os.path.exists(file_path) and os.path.getsize(file_path) <= max_attachment_size_bytes:
                    return {'status': 'Success', 'path': file_path, 'error_message': 'File already exists.'}

                return {'status': 'Success', 'path': file_path, 'error_message': ''}

            else:
                return {'status': 'Failure', 'path': '', 'error_message': f"File not found: {file_source}"}

        elif hasattr(file_source, 'read') and callable(file_source.read):
            file_data = file_source.read()
            temp_folder = os.path.join(os.getcwd(), 'payomail', 'temp')
            os.makedirs(temp_folder, exist_ok=True)
            file_path = os.path.join(temp_folder, 'downloaded_file.bin')

            # Check if the file already exists and has the same size
            if os.path.exists(file_path) and os.path.getsize(file_path) == len(file_data):
                return {'status': 'Success', 'path': file_path, 'error_message': 'File already exists.'}

            # Check if the file size exceeds the maximum allowed size
            if len(file_data) > max_attachment_size_bytes:
                return {'status': 'Failure', 'path': '', 'error_message': f"File size exceeds the maximum allowed size ({max_attachment_size_bytes} bytes)."}

            with open(file_path, 'wb') as file:
                file.write(file_data)

            return {'status': 'Success', 'path': file_path, 'error_message': ''}

        else:
            return {'status': 'Failure', 'path': '', 'error_message': 'Invalid file source. Please provide a valid file path or URL.'}

    except requests.exceptions.RequestException as e:
        return {'status': 'Failure', 'path': '', 'error_message': f"Error downloading file: {str(e)}"}

    except Exception as e:
        return {'status': 'Failure', 'path': '', 'error_message': f"An unexpected error occurred: {str(e)}"}


def get_size_by_path(file_path):
    """
    Get the size of a file specified by its path.

    Parameters:
        file_path (str): The path of the file.

    Returns:
        int: Size of the file in bytes.
    """
    if os.path.exists(file_path):
        return os.path.getsize(file_path)
    else:
        raise FileNotFoundError(f"File not found: {file_path}")